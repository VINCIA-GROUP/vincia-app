class AbilityService:
    def __init__(self, ability_rating_repository):
        self.ability_rating_repository = ability_rating_repository
    
    def get_average_rating(self, user_id):
        abilities = self.ability_rating_repository.get_current_rating(user_id)

        rating_sum = 0
        count = 0
        for ability in abilities:
            id, rating = ability
            rating_sum += rating
            count += 1
            
        try:
            result = float(rating_sum)/float(count)
            return {'rating' : int(result)}
        except:
            return {'rating' : 0}
            
        