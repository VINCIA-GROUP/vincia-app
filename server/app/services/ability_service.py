import uuid
from datetime import datetime


class AbilityService:
    
    rating = 100
    rating_deviation = 350
    volatility = 0.6
    
    def __init__(self, ability_rating_repository, abilities_repository):
        self.ability_rating_repository = ability_rating_repository
        self.abilities_repository = abilities_repository
    
    def get_average_rating(self, user_id):   
        try:
            abilities = self.ability_rating_repository.get_current_rating(user_id)
            
            rating_sum = 0
            count = 0
            for ability in abilities:
                id, rating = ability
                rating_sum += rating
                count += 1
            result = float(rating_sum)/float(count)
            return {'rating' : int(result)}
        except:
            return {'rating' : 0}
            
    def create_abilities(self, user_id):
        abilities = self.abilities_repository.get_all()
        for ability in abilities:
            self.ability_rating_repository.create(str(uuid.uuid4()), self.rating, self.rating_deviation, self.volatility, ability.id, user_id, datetime.utcnow())