from infra.repositories.repository import Repository


class HistoryOfUserRatingUpdateRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
    
    def create(self, entity):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO history_of_user_rating_updates (id, create_at, rating, rating_deviation, volatility,  user_id, ability_id) VALUES (%s, %s, %s, %s, %s, %s, %s);", (entity.id, entity.create_at, entity.rating, entity.rating_deviation, entity.volatility, entity.user_id, entity.ability_id))
        cursor.close()
        
