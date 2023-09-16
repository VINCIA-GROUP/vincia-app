from datetime import datetime, timedelta
import uuid
from app.domain.entities.history_of_user_rating_update import HistoryOfUserRatingUpdate
from app.services import glicko2


class RatingService:
    
    tau = 0.1
    day_to_update = 1
    
    def __init__(self, history_question_repository, history_of_user_rating_update_repository, abilities_rating_repository, question_repository, history_of_question_rating_update_repository, ability_service):
        self.history_question_repository = history_question_repository
        self.history_of_user_rating_update_repository = history_of_user_rating_update_repository
        self.abilities_rating_repository = abilities_rating_repository
        self.question_repository = question_repository
        self.history_of_question_rating_update_repository = history_of_question_rating_update_repository
        self.ability_service = ability_service
    
    def check_rating_user(self, user_id):
        date = self.history_of_user_rating_update_repository.get_date_last_update(user_id)
        update_time = (datetime.utcnow() + timedelta(days=self.day_to_update)).date()
        if(date == None or date > update_time):
            abilities = self.history_question_repository.get_all_abilities_history_without_rating_id(user_id) 
            if(abilities == None):
                self.update_user_rating(user_id, None)     
                return  
            for ability in abilities:
                self.update_user_rating(user_id, ability)
            
    
    def check_rating_question(self, question_id):
        last_rating_update = self.question_repository.get_date_last_update(question_id)
        update_time = (datetime.utcnow() + timedelta(days=self.day_to_update)).date()
        if(last_rating_update >  update_time):                
            self.update_rating_question(question_id)
            
            
    def update_user_rating(self, user_id, ability_id):
        
        ability = self.abilities_rating_repository.get_by_id(ability_id, user_id)
        if(ability == None):
            self.ability_service.create_abilities(user_id)
            return
            
        glicko = glicko2.Player(rating= ability.rating, rd= ability.rating_deviation, vol =ability.volatility)
        
        histories = self.history_question_repository.get_all_history_without_rating_id(user_id, ability_id)

        if(histories == None or len(histories) <= 0):
            glicko.did_not_compete()
        else:
            rating_list, RD_list, outcome_list = self._get_history_values(histories)  
            glicko.update_player(rating_list, RD_list, outcome_list)
        
        history_of_user_rating_update_id = str(uuid.uuid4())
        self.history_of_user_rating_update_repository.create(HistoryOfUserRatingUpdate(history_of_user_rating_update_id, datetime.utcnow(), glicko.getRating(), glicko.getRd(), glicko.vol, user_id, ability_id))
        self.abilities_rating_repository.update_rating(ability.id, glicko.getRating(), glicko.getRd(), glicko.vol, user_id)
        
        for history in histories:            
            self.history_question_repository.update_rating(history.id, user_id, history_of_user_rating_update_id)

        
    def update_rating_question(self, question_id):
        question = self.question_repository.get_by_id(question_id)
            
        glicko = glicko2.Player(rating= question.rating, rd= question.rating_deviation, vol =question.volatility, tau=self.tau)
        
        histories = self.history_question_repository.get_all_histories(question.last_rating_update, question.id)
        
        if(histories == None or len(histories) <= 0):
            glicko.did_not_compete()
        else:
            rating_list = []
            RD_list = []
            outcome_list = []
            for history in histories:
                id, hit_level, rating, rating_deviation, volatility = history
                rating_list.append(rating)
                RD_list.append(rating_deviation)
                outcome_list.append(abs(hit_level - 1))
            
            glicko.update_player(rating_list, RD_list, outcome_list)
        
        self.question_repository.update_rating(question.id, glicko.getRating(), glicko.getRd(), glicko.vol, datetime.utcnow())
        self.history_of_question_rating_update_repository.create(str(uuid.uuid4()), datetime.utcnow(), glicko.getRating(), glicko.getRd(), glicko.vol, question.id)
        
    def _get_history_values(self, histories):
        rating_list = []
        RD_list = []
        outcome_list = []    
        for history in histories:
            question = self.question_repository.get_by_id_without_alternatives(history.question_id)
            rating_list.append(question.rating)
            RD_list.append(question.rating_deviation)
            outcome_list.append(history.hit_level)
        return (rating_list, RD_list, outcome_list)
