from app.domain.entities.history_of_question_rating_update import HistoryOfQuestionRatingUpdate
from app.domain.entities.history_of_user_rating_update import HistoryOfUserRatingUpdate
from app.domain.errors.api_exception import *
from datetime import datetime, timedelta
import random
import uuid

from app.domain.errors.domain_errors import AbilityNotFound, AbilityRatingCreateFailed, HistoryOfQuestionIdInvalid, QuestionNotFound
from app.services import glicko2

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
        
        self.calculate_rating_user_and_return_ability_id(user_id)
        abilities_restrictions = self.history_of_user_rating_update_repository.get_ability_id_last_updates(user_id, 3)
        
        abilities = self.get_all_abilities(user_id)
        
        questions = []
        for ability in abilities:
            
            ability_rating, ability_id = ability
            if abilities_restrictions != None and ability_id in abilities_restrictions:
                continue
            
            random_number = random.uniform(-0.2, 0.2)
            random_ability_rating = ability_rating * random_number
            
            questions = self.question_repository.get_by_rating(random_ability_rating, limit_question, ability_id)
            
            result_history_id = str(uuid.uuid4())
            for question in questions:
                history_id = str(uuid.uuid4())
                if question.id == questions[0].id:
                    history_id = result_history_id
                self.history_question_repository.create(history_id, datetime.utcnow(), question.id, user_id)
                
            if len(questions) > 0:
                self.history_question_repository.commit();          
                return {"historyOfQuestion": result_history_id, "question":questions[0].to_json()}

            abilities_restrictions.append(ability_id)
            
        raise ApiException(QuestionNotFound())

        
    def get_all_abilities(self, user_id):
        abilities = self.abilities_rating_repository.get_all_ability_id_and_rating(user_id)
        if(abilities  == None):
            self.create_abilities(user_id)
            abilities = self.abilities_rating_repository.get_all_ability_id_and_rating(user_id)
        return abilities
        
    
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
        if(histories == None or len(histories) <= 0):
            return None
        rating_list = []
        RD_list = []
        outcome_list = []    
        for history in histories:
            question = self.question_repository.get_by_id(history.question_id)
            rating_list.append(question.rating)
            RD_list.append(question.rating_deviation)
            outcome_list.append(history.hit_level)
            ability_id = question.ability_id
            
        ability = self.abilities_rating_repository.get_by_id(ability_id, user_id)
        
        glicko = glicko2.Player(rating= ability.rating, rd= ability.rating_deviation, vol =ability.volatility)
        glicko.update_player(rating_list, RD_list, outcome_list)
        
        history_of_user_rating_update_id = str(uuid.uuid4())
        self.history_of_user_rating_update_repository.create(HistoryOfUserRatingUpdate(history_of_user_rating_update_id, datetime.utcnow(), glicko.getRating(), glicko.getRd(), glicko.vol, user_id, ability_id))
        self.abilities_rating_repository.update_rating(ability.id, glicko.getRating(), glicko.getRd(), glicko.vol, user_id)
        
        for history in histories:            
            self.history_question_repository.update_calculate_rating(history.id, user_id, True, history_of_user_rating_update_id )

    def create_abilities(self, user_id):
        rating = 1500
        rating_deviation = 350
        volatility = 0.6
        abilities = self.abilities_repository.get_all()
        for ability in abilities:
            self.abilities_rating_repository.create(str(uuid.uuid4()), rating, rating_deviation, volatility, ability.id, user_id)

        
    def update_rating_question(self, question, user_id):
        tau = 0.1
        update_time = (datetime.utcnow() + timedelta(days=1)).date()
        if(question.last_rating_update <  update_time):
            histories = self.history_question_repository.get_all_histories(question.last_rating_update, question.id)
            if(histories == None or len(histories) <= 0):
                return
            rating_list = []
            RD_list = []
            outcome_list = []
            for history in histories:
                id, hit_level, rating, rating_deviation, volatility = history
                rating_list.append(rating)
                RD_list.append(rating_deviation)
                outcome_list.append(abs(hit_level - 1))
                
            glicko = glicko2.Player(rating= question.rating, rd= question.rating_deviation, vol =question.volatility)
            glicko.update_player(rating_list, RD_list, outcome_list)
            
            self.question_repository.update_rating(question.id, glicko.getRating(), glicko.getRd(), glicko.vol)
            self.history_of_question_rating_update_repository.create(id=str(uuid.uuid4()), create_at=datetime.utcnow(), rating=glicko.getRating(), rating_deviation=glicko.getRd(), volatility=glicko.vol, question_id=question.id)
        