from psycopg2 import DatabaseError
from domain.entities.ability_rating import AbilityRating

class AbilitiesRatingRepository():
    def __init__(self, connection): 
        self.connection = connection  
        
    def get_min_rating(self, restriction, user_id):
        ability_rating = AbilityRating() 
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT q.rating, q.ability_id FROM abilities_rating q WHERE q.user_id = %s AND q.id != %s ORDER BY rating LIMIT 1;", (user_id, restriction))
            row = cursor.fetchone()
            ability_rating = AbilityRating(*row)
            cursor.close()
        except DatabaseError as error:
            print('AbilitiesRatingRepository - get_min_rating - ' + error)
        return ability_rating
    
    def get_by_id(self, ability_id, user_id):
        ability_rating = AbilityRating()
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT q.id, q.rating, q.rating_deviation, q.volatility, q.ability_id, q.user_id FROM abilities_rating q WHERE q.user_id = %s AND q.ability_id = %s", (user_id, ability_id))
            row = cursor.fetchone()
            ability_rating = AbilityRating(*row)
            cursor.close()
        except DatabaseError as error:
            print('AbilitiesRatingRepository - get_min_rating - ' + error)
        return ability_rating
    
    def create(self, id, rating, rating_deviation, volatility, ability_id, user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("INSERT INTO abilities_rating (id, rating, rating_deviation, volatility, ability_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);", (id, rating, rating_deviation, volatility, ability_id, user_id))
            cursor.close()
            return True
        except DatabaseError as error:        
            print('AbilitiesRatingRepository - create - ' + error)
            return False
    
    def update(self, id, rating, rating_deviation, volatility , user_id):
        try:
            cursor = self.conn.cursor()
            cursor.execute("UPDATE abilities_rating SET rating = %s, rating_deviation = %s, volatility = %s WHERE id = %s AND user_id = %s;", (rating, rating_deviation, volatility, id, user_id))
            cursor.close()
            return True
        except DatabaseError as error:
            print('AbilitiesRatingRepository - update - ' + error)
            return False
        
    def commit(self):
        try:
            self.connection.commit()
            return True
        except DatabaseError as error:
            print('QuestionsRepository - commit - ' + error)
            return False
      
    def rollback(self):
        try:
            self.connection.rollback()
            return True
        except DatabaseError as error:
            print('QuestionsRepository - rollback - ' + error)
            return False