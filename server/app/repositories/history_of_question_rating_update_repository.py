
class HistoryOfQuestionRatingUpdateRepository():
    def __init__(self, connect): 
        super().__init__(connect) 
        
    def create(self, id, create_at, rating, rating_deviation, volatility,  question_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO history_of_question_rating_updates (id, create_at, rating, rating_deviation, volatility,  question_id) VALUES (%s, %s, %s, %s, %s, %s);", (id, create_at, rating, rating_deviation, volatility, question_id))
        cursor.close()