from domain.entities.ability_rating import AbilityRating
from infra.repositories.repository import Repository


class AbilitiesRatingRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_ability_with_min_rating(self, restriction, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.rating, q.ability_id FROM abilities_rating q WHERE q.user_id = %s AND q.id != %s ORDER BY rating LIMIT 1;", (user_id, restriction))
        if(cursor.rowcount <= 0):
            cursor.close()
            return (None, None)
        rating, ability_id = cursor.fetchone()
        cursor.close()
        return (rating, ability_id)
    
    def get_ability_by_id(self, ability_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.rating, q.rating_deviation, q.volatility, q.ability_id, q.user_id FROM abilities_rating q WHERE q.user_id = %s AND q.ability_id = %s", (user_id, ability_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, rating, rating_deviation, volatility, ability_id, user_id = cursor.fetchone()
        ability = AbilityRating(id, rating, rating_deviation, volatility, ability_id, user_id)
        cursor.close()
        return ability
    
    def create(self, id, rating, rating_deviation, volatility, ability_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO abilities_rating (id, rating, rating_deviation, volatility, ability_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);", (id, rating, rating_deviation, volatility, ability_id, user_id))
        cursor.close()
        return (rating, ability_id)
    
    def update_rating(self, id, rating, rating_deviation, volatility , user_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE abilities_rating SET rating = %s, rating_deviation = %s, volatility = %s WHERE id = %s AND user_id = %s;", (rating, rating_deviation, volatility, id, user_id))
        cursor.close()