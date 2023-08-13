from app.repositories.repository import Repository

class HistoryOfQuestionRatingUpdateRepository(Repository):
    def __init__(self, connection): 
        super().__init__(connection, "")  
        
    def create(self, id, create_at, rating, rating_deviation, volatility,  question_id):
        return super().update(
            query="INSERT INTO history_of_question_rating_updates (id, create_at, rating, rating_deviation, volatility,  question_id) VALUES (%s, %s, %s, %s, %s, %s);",
            params=(id, create_at, rating, rating_deviation, volatility, question_id)
        )