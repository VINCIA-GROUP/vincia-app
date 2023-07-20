from domain.entities.history_of_user_rating_update import HistoryOfUserRatingUpdate
from infra.repositories.repository import Repository


class HistoryOfUserRatingUpdateRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
    
    def create(self, entity):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO history_of_user_rating_updates (id, create_at, rating, rating_deviation, volatility,  user_id) VALUES (%s, %s, %s, %s, %s, %s);", (entity.id, entity.create_at, entity.rating, entity.rating_deviation, entity.volatility, entity.user_id))
        cursor.close()
        
    def get_all(self, date, question_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, create_at, rating, rating_deviation, volatility, user_id FROM history_of_user_rating_updates WHERE id = (SELECT id FROM history_of_questions WHERE question_id = %s AND user_id = %s AND answer_at > %s)", (question_id, user_id, date))
        histories_tuple = cursor.fetchall()
        list_result = []
        for history_tuple in histories_tuple:
            id, create_at, rating, rating_deviation, volatility, user_id = histories_tuple
            list_result.append(HistoryOfUserRatingUpdate(id, create_at, rating, rating_deviation, volatility, user_id))            
        cursor.close()
        return list_result