from domain.errors.api_exception import *
from datetime import datetime
import uuid

from domain.errors.domain_errors import AbilityNotFound, HistoryOfQuestionIdInvalid, QuestionNotFound

class QuestionService:
    def __init__(self, question_repository, history_question_repository, abilities_rating_repository, abilities_repository):
        self.question_repository = question_repository
        self.history_question_repository = history_question_repository
        self.abilities_rating_repository = abilities_rating_repository
        self.abilities_repository = abilities_repository
    
    def get_question(self, user_id):
        
        limit_question = 10
        rating = 1500
        rating_deviation = 350
        volatility = 0.6
    
        history_of_question = self.history_question_repository.get_history_without_answer(user_id)
        if(history_of_question != None):
            # Verify and Update Question
            question = self.question_repository.get_by_id(history_of_question.question_id)
            return {"historyOfQuestion": history_of_question.id, "question": question.to_json()}

        # Calcular nova nota usuario
        ability_id_exception = None
        ability_rating = self.abilities_rating_repository.get_ability_with_min_rating(ability_id_exception, user_id)
        if(ability_rating  == None):
            abilities = self.abilities_repository.get_abilities_list()
            for ability in abilities:
                self.abilities_rating_repository.create(str(uuid.uuid4()), rating, rating_deviation, volatility, ability.id, user_id)
            ability_rating = self.abilities_rating_repository.get_ability_with_min_rating(ability_id_exception, user_id)
        
        questions = self.question_repository.get_question_by_rating(ability_rating, limit_question)
        result_history_id = str(uuid.uuid4())
        for question in questions:
            history_id = str(uuid.uuid4())
            if question.id == questions[0].id:
                history_id = result_history_id
            self.history_question_repository.create(history_id, datetime.now(), question.id, user_id)
        
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
        
        self.history_question_repository.insert_answer(history_question_id, datetime.now(), hit_level, duration, user_id)
        self.history_question_repository.commit()
        
    def verify_answer(self, answer, question):
        if question.is_essay:
            raise Exception("Essay questions not implemented")
        else:
            if question.answer == answer:
                return 1
            return 0