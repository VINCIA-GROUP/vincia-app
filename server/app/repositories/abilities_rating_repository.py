from app.domain.entities.ability_rating import AbilityRating
from app.repositories.repository import Repository

class AbilitiesRatingRepository(Repository):
    def __init__(self, connection): 
        super().__init__(connection, AbilityRating)  
        
    def get_min_rating(self, restriction, user_id):
        return super().get_one(
            query="SELECT q.rating, q.ability_id FROM abilities_rating q WHERE q.user_id = %s AND q.id != %s ORDER BY rating LIMIT 1;", 
            params=(user_id, restriction)
        )
    
    def get_by_id(self, ability_id, user_id):
        return super().get_one(
            query="SELECT q.id, q.rating, q.rating_deviation, q.volatility, q.ability_id, q.user_id FROM abilities_rating q WHERE q.user_id = %s AND q.ability_id = %s",
            params=(user_id, ability_id)
        )
    
    def create(self, id, rating, rating_deviation, volatility, ability_id, user_id):
        return super().update(
            query="INSERT INTO abilities_rating (id, rating, rating_deviation, volatility, ability_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);",
            params=(id, rating, rating_deviation, volatility, ability_id, user_id)
        )
    
    def update(self, id, rating, rating_deviation, volatility , user_id):
        return super().update(
            query="UPDATE abilities_rating SET rating = %s, rating_deviation = %s, volatility = %s WHERE id = %s AND user_id = %s;",
            params=(rating, rating_deviation, volatility, id, user_id)
        )