from domain.entities.ability_rating import AbilityRating
from infra.repositories.repository import Repository


class AbilitiesRatingRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_ability_with_min_rating(self, restriction, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.rating FROM abilities_rating q WHERE q.user_id = %s AND q.id != %s ORDER BY rating LIMIT 1;", (user_id, restriction))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        rating= cursor.fetchone()
        cursor.close()
        return rating[0]
    
    def get_ability_by_id(self, abilitie_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.rating, q.rating_deviation, q.volatility, q.abilitie_id, q.user_id FROM abilities_rating q WHERE q.user_id = %s AND q.abilitie_id", (user_id, abilitie_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, rating, rating_deviation, volatility, abilitie_id, user_id = cursor.fetchone()
        ability = AbilityRating(id, rating, rating_deviation, volatility, abilitie_id, user_id)
        cursor.close()
        return ability
    
    def create(self, id, rating, rating_deviation, volatility, ability_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO abilities_rating (id, rating, rating_deviation, volatility, ability_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);", (id, rating, rating_deviation, volatility, ability_id, user_id))
        cursor.close()
        return rating
    
    def update_rating(self, id, rating, rating_deviation, volatility , user_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE abilities_rating SET rating = %s, rating_deviation = %s, volatility = %s WHERE id = %s AND user_id = %s;", (rating, rating_deviation, volatility, id, user_id))
        cursor.close()