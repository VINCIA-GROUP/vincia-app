from datetime import datetime, timedelta
import uuid
from app.domain.entities.history_of_user_rating_update import HistoryOfUserRatingUpdate
from app.services import glicko2


class RatingService:
    
    tau = 0.1
    
    def __init__(self, history_question_repository, history_of_user_rating_update_repository, abilities_rating_repository, question_repository, history_of_question_rating_update_repository, ability_service):
        self.history_question_repository = history_question_repository
        self.history_of_user_rating_update_repository = history_of_user_rating_update_repository
        self.abilities_rating_repository = abilities_rating_repository
        self.question_repository = question_repository
        self.history_of_question_rating_update_repository = history_of_question_rating_update_repository
        self.ability_service = ability_service
    
    def check_rating_user(self, user_id):
        list_abilities = self.abilities_rating_repository.get_all_ability(user_id)
        current_date = datetime.utcnow().date()
        for ability in list_abilities:
            data_range = range((current_date - ability.last_rating_update).days + 1)
            for i in data_range:
                if i <= 0:
                    continue
                temp_date = current_date - timedelta(days=i)
                ability = self.update_user_rating(user_id, ability, temp_date)
            self.abilities_rating_repository.update_rating(ability.id, ability.rating, ability.rating_deviation, ability.volatility, user_id, datetime.utcnow())
            
            
    
    def check_rating_question(self, question_id):
        last_rating_update = self.question_repository.get_date_last_update(question_id)
        update_time = (datetime.utcnow() + timedelta(days=1)).date()
        if(last_rating_update >  update_time):                
            self.update_rating_question(question_id)
            
            
    def update_user_rating(self, user_id, ability, date):
            
        glicko = glicko2.Player(rating= ability.rating, rd= ability.rating_deviation, vol =ability.volatility)
        
        histories = self.history_question_repository.get_all_history_without_rating_id(user_id, ability.ability_id, date)

        if(histories == None or len(histories) <= 0):
            glicko.did_not_compete()
        else:
            rating_list, RD_list, outcome_list = self._get_history_values(histories)  
            glicko.update_player(rating_list, RD_list, outcome_list)
        
        history_of_user_rating_update_id = str(uuid.uuid4())
        self.history_of_user_rating_update_repository.create(HistoryOfUserRatingUpdate(history_of_user_rating_update_id, datetime.utcnow(), glicko.getRating(), glicko.getRd(), glicko.vol, user_id, ability.ability_id))
        
        ability.update(glicko.getRating(), glicko.getRd(), glicko.vol)
        
        for history in histories:            
            self.history_question_repository.update_rating(history.id, user_id, history_of_user_rating_update_id)
            
        return ability

        
    def update_rating_question(self, question_id):
        question = self.question_repository.get_by_id(question_id)
            
        glicko = glicko2.Player(rating= question.rating, rd= question.rating_deviation, vol =question.volatility, tau=self.tau)
        
        histories = self.history_question_repository.get_all_histories(question.last_rating_update, question.id)
        
        if(histories == None or len(histories) <= 0):
            return
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
