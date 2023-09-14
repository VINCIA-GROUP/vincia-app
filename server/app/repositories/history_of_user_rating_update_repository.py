from app.repositories.repository import Repository

class HistoryOfUserRatingUpdateRepository(Repository):
    def __init__(self, connection): 
        super().__init__(connection, "")   
    
    def create(self, entity):
        return super().update(
            query="INSERT INTO history_of_user_rating_updates (id, create_at, rating, rating_deviation, volatility,  user_id, ability_id) VALUES (%s, %s, %s, %s, %s, %s, %s);",
            params=(entity.id, entity.create_at, entity.rating, entity.rating_deviation, entity.volatility, entity.user_id, entity.ability_id)
        )
        
    def get_date_last_update(self, user_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT create_at FROM history_of_user_rating_updates WHERE user_id = %s ORDER BY create_at LIMIT 1', (user_id,))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        result, = cursor.fetchone() 
        cursor.close()
        return result
        
    def get_ability_id_last_updates(self, user_id, quantity):
        cursor = self.connection.cursor()
        cursor.execute('SELECT DISTINCT ability_id FROM (SELECT ability_id, create_at FROM history_of_user_rating_updates WHERE user_id = %s ORDER BY create_at) AS subquery GROUP BY ability_id LIMIT %s', (user_id, quantity))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        datas = cursor.fetchall() 
        result = []
        for data in datas:
            id, = data
            result.append(id)
        cursor.close()
        return result