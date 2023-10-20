from app.domain.entities.adaptive_question_selection import AdaptiveQuestionSelection
from app.domain.errors.api_exception import *
from datetime import datetime
import random
import uuid

from app.domain.errors.domain_errors import QuestionNotFound
from app.services import glicko2

class QuestionService:
    
    max_question = 10
    min_question = 5
    abilities_restrictions_num = 5
    
    def __init__(self, question_repository, history_question_repository, abilities_rating_repository, history_of_user_rating_update_repository,  adaptive_question_selection_repository, ability_service, rating_service):
        self.question_repository = question_repository
        self.history_question_repository = history_question_repository
        self.abilities_rating_repository = abilities_rating_repository
        self.history_of_user_rating_update_repository = history_of_user_rating_update_repository
        self.adaptive_question_selection_repository = adaptive_question_selection_repository
        self.ability_service = ability_service
        self.rating_service = rating_service
    
    def get_question(self, user_id):

        selection_question = self.adaptive_question_selection_repository.get_any(user_id)
        if(selection_question != None):
            question = self.question_repository.get_by_id(selection_question.question_id)
            self.rating_service.check_rating_question(question.id)
            self.adaptive_question_selection_repository.remove_by_id(selection_question.id, user_id)
            self.question_repository.commit(); 
            return {"question": question.to_json()}
        
        self.rating_service.check_rating_user(user_id)
        
        abilities_restrictions = self.history_question_repository.get_last_abilities_use(self.abilities_restrictions_num, user_id)
        
        abilities = self._get_all_abilities(user_id)
        
        questions = []
        for ability in abilities:
            
            ability_rating, ability_id = ability
            if abilities_restrictions != None and ability_id in abilities_restrictions:
                continue
            
            questions = self._select_question(ability_rating, ability_id)
            
            selection_question_id = self._create_question_selection(questions, user_id)
                
            if len(questions) > 0:
                self.adaptive_question_selection_repository.remove_by_id(selection_question_id, user_id)
                self.question_repository.commit();          
                return {"question":questions[0].to_json()}

            abilities_restrictions.append(ability_id)
            
        raise ApiException(QuestionNotFound())
    
    def insert_question_answer(self, question_id, user_id, answer, duration):              
        question = self.question_repository.get_by_id(question_id)
        if(question == None):
            raise ApiException(QuestionNotFound())
        hit_level = self._verify_answer(answer, question)
        new_id = str(uuid.uuid4())
        self.history_question_repository.create(new_id, datetime.utcnow(), hit_level, duration, question.id, user_id)
        self.history_question_repository.commit()
        return {"historyQuestionId":new_id} 
    
    def _create_question_selection(self, questions, user_id):
        result = None
        for question in questions:
            new_id = str(uuid.uuid4())
            if result == None:
                result = new_id
            entity = AdaptiveQuestionSelection(new_id, datetime.utcnow(), question.id, user_id)
            self.adaptive_question_selection_repository.insert(entity)
        return result
    

    def _select_question(self, ability_rating, ability_id):
        random_number = random.uniform(-0.2, 0.2)
        random_question = random.uniform(self.min_question, self.max_question)
        random_ability_rating = ability_rating + ability_rating * random_number
        return self.question_repository.get_by_rating(random_ability_rating, random_question, ability_id) 
    
    
    def _get_all_abilities(self, user_id):
        abilities = self.abilities_rating_repository.get_all_ability_id_and_rating(user_id)
        if(abilities  == None):
            self.ability_service.create_abilities(user_id)
            abilities = self.abilities_rating_repository.get_all_ability_id_and_rating(user_id)
        return abilities
  
    def _verify_answer(self, answer, question):
        if question.is_essay:
            raise Exception("Essay questions is not implemented")
        else:
            if question.answer == answer:
                return 1
            return 0
