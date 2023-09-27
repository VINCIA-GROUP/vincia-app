from app.domain.entities.ability_rating import AbilityRating
from app.repositories.repository import Repository

class AbilitiesRatingRepository(Repository):
    def __init__(self, connection): 
        super().__init__(connection, AbilityRating)  
        
    def get_all_ability_id_and_rating(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT q.rating, q.ability_id FROM abilities_rating AS q WHERE q.user_id = %s ORDER BY rating*random();', (user_id, ))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        result = cursor.fetchall() 
        cursor.close()
        return result
    
    def get_all_ability(self, user_id):
        return super().get_many(
            query="SELECT q.id, q.rating, q.rating_deviation, q.volatility, q.ability_id, q.user_id, q.last_rating_update FROM abilities_rating q WHERE q.user_id = %s;",
            params=(user_id,)
        )
        
  
    def get_by_id(self, ability_id, user_id):
        return super().get_one(
            query="SELECT q.id, q.rating, q.rating_deviation, q.volatility, q.ability_id, q.user_id, q.last_rating_update FROM abilities_rating q WHERE q.user_id = %s AND q.ability_id = %s",
            params=(user_id, ability_id)
        )
        
    def get_current_rating(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT DISTINCT a.id, a.rating FROM abilities_rating a JOIN history_of_user_rating_updates h ON a.ability_id = h.ability_id  WHERE a.user_id = %s AND h.create_at >= CURRENT_DATE - INTERVAL '1 month';", (user_id,))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        result = cursor.fetchall()
        cursor.close()
        return result
    
    def create(self, id, rating, rating_deviation, volatility, ability_id, user_id, last_rating_update):
        super().update(
            query="INSERT INTO abilities_rating (id, rating, rating_deviation, volatility, ability_id, user_id, last_rating_update) VALUES (%s, %s, %s, %s, %s, %s, %s);",
            params=(id, rating, rating_deviation, volatility, ability_id, user_id, last_rating_update)
        )
    
    def update_rating(self, id, rating, rating_deviation, volatility , user_id, last_rating_update):
        super().update(
            query="UPDATE abilities_rating SET rating = %s, rating_deviation = %s, volatility = %s, last_rating_update = %s WHERE id = %s AND user_id = %s;",
            params=(rating, rating_deviation, volatility, last_rating_update, id, user_id)
        )