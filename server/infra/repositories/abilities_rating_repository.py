from infra.repositories.repository import Repository


class AbilitiesRatingRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_ability_with_min_rating(self, exception, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.rating FROM abilities_rating q WHERE q.user_id = %s AND q.id != %s ORDER BY rating LIMIT 1;", (user_id, exception))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        rating= cursor.fetchone()
        cursor.close()
        return rating[0]
    
    def create(self, id, rating, rating_deviation, volatility, ability_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO abilities_rating (id, rating, rating_deviation, volatility, ability_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);", (id, rating, rating_deviation, volatility, ability_id, user_id))
        cursor.close()
        return rating