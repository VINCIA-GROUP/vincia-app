from domain.entities.history_of_question_rating_update import HistoryOfQuestionRatingUpdate
from domain.entities.history_of_user_rating_update import HistoryOfUserRatingUpdate
from domain.errors.api_exception import *
from datetime import datetime, timedelta
import uuid

from domain.errors.domain_errors import AbilityNotFound, HistoryOfQuestionIdInvalid, QuestionNotFound
from services import glicko2

class QuestionService:
    def __init__(self, question_repository, history_question_repository, abilities_rating_repository, abilities_repository, history_of_user_rating_update_repository, history_of_question_rating_update_repository):
        self.question_repository = question_repository
        self.history_question_repository = history_question_repository
        self.abilities_rating_repository = abilities_rating_repository
        self.abilities_repository = abilities_repository
        self.history_of_user_rating_update_repository = history_of_user_rating_update_repository
        self.history_of_question_rating_update_repository = history_of_question_rating_update_repository
    
    def get_question(self, user_id):
        limit_question = 10
        
        history_of_question = self.history_question_repository.get_history_without_answer(user_id)
        if(history_of_question != None):
            question = self.question_repository.get_by_id(history_of_question.question_id)
            self.update_rating_question(question, user_id)
            self.history_question_repository.commit(); 
            return {"historyOfQuestion": history_of_question.id, "question": question.to_json()}
        
        ability_id_restriction = self.calculate_rating_user_and_return_ability_id(self, user_id)
        
        ability_rating = self.abilities_rating_repository.get_ability_with_min_rating(ability_id_restriction, user_id)
        if(ability_rating  == None):
            ability_rating = self.create_abilities(user_id, ability_id_restriction)
        
        questions = self.question_repository.get_question_by_rating(ability_rating, limit_question)
        result_history_id = str(uuid.uuid4())
        for question in questions:
            history_id = str(uuid.uuid4())
            if question.id == questions[0].id:
                history_id = result_history_id
            self.history_question_repository.create(history_id, datetime.utcnow(), question.id, user_id)
        
        self.history_question_repository.commit();          
        return {"historyOfQuestion": result_history_id, "question":questions[0].to_json()}
    
    def insert_question_answer(self, history_question_id, user_id, answer, duration):   
        try:
            uuid_obj = uuid.UUID(history_question_id)
        except ValueError:
            raise ApiException(HistoryOfQuestionIdInvalid())
            
        question = self.history_question_repository.get_question(history_question_id, user_id)
        if(question == None):
            raise ApiException(QuestionNotFound())
        
        hit_level = self.verify_answer(answer, question)
        
        self.history_question_repository.insert_answer(history_question_id, datetime.utcnow(), hit_level, duration, user_id)
        self.history_question_repository.commit()
        
    def verify_answer(self, answer, question):
        if question.is_essay:
            raise Exception("Essay questions not implemented")
        else:
            if question.answer == answer:
                return 1
            return 0
        
    def calculate_rating_user_and_return_ability_id(self, user_id):
        histories = self.history_question_repository.get_all_history_without_calculate_rating(user_id)
        rating_list, RD_list, outcome_list = []
        ability_id = None
        history_of_user_rating_update_id = str(uuid.uuid4())
        for history in histories:
            question = self.question_repository.get_by_id(history.question_id)
            rating_list.append(question.rating)
            RD_list.append(question.rating_deviation)
            outcome_list.append(question.volatility)
            ability_id = question.ability_id
            self.history_question_repository.update_calculate_rating(history.id, user_id, True, history_of_user_rating_update_id )
        
        ability = self.abilities_rating_repository.get_ability_by_id(ability_id, user_id)
        
        glicko = glicko2.Player(rating= ability.rating, rd= ability.rating_deviation, vol =ability.volatility)
        glicko.update_player(rating_list, RD_list, outcome_list)
        
        self.history_of_user_rating_update_repository.create(HistoryOfUserRatingUpdate(history_of_user_rating_update_id, datetime.utcnow(), glicko.getRating(), glicko.getRd(), glicko.vol, user_id))
        self.abilities_rating_repository.update_rating(ability.id, glicko.getRating(), glicko.getRd(), glicko.vol, user_id)
        
        return ability.id
    
    def create_abilities(self, user_id, ability_id_restriction):
        rating = 1500
        rating_deviation = 350
        volatility = 0.6
        abilities = self.abilities_repository.get_abilities_list()
        for ability in abilities:
            self.abilities_rating_repository.create(str(uuid.uuid4()), rating, rating_deviation, volatility, ability.id, user_id)
        return self.abilities_rating_repository.get_ability_with_min_rating(ability_id_restriction, user_id)
    
    def update_rating_question(self, question, user_id):
        tau = 0.1
        update_time_days = timedelta(days=1)
        if(question.last_rating_update <  datetime.utcnow() - update_time_days):
            histories = self.history_of_user_rating_update_repository.get_all(question.last_rating_update, question.id, user_id)
            rating_list, RD_list, outcome_list = []
            for history in histories:
                rating_list.append(history.rating)
                RD_list.append(history.rating_deviation)
                outcome_list.append(history.volatility)
                
            glicko = glicko2.Player(rating= question.rating, rd= question.rating_deviation, vol =question.volatility)
            glicko.update_player(rating_list, RD_list, outcome_list)
            
            self.question_repository.update_rating(question.id, glicko.getRating(), glicko.getRd(), glicko.vol)
            self.history_of_question_rating_update_repository.create(HistoryOfQuestionRatingUpdate(str(uuid.uuid4()), datetime.utcnow(), glicko.getRating(), glicko.getRd(), glicko.vol, question.id))