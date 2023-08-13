from app.domain.entities.history_of_question import HistoryOfQuestion
from app.repositories.repository import Repository

class HistoryOfQuestionRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_by_id(self, id, user_id):
        return super().get_one(
            query="SELECT * FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", 
            params=(id,user_id)
        )
    
    def get_history_without_answer(self, user_id):
        return super().get_many(
            query="SELECT * FROM history_of_questions q WHERE q.user_id = %s AND q.answer_at IS NULL;",
            params=(user_id,)
        )
        
    def get_all_history_without_calculate_rating(self, user_id):
        return super().get_many(
            query="SELECT q.id, q.create_at, q.answer_at, q.hit_level, q.time, q.question_id, q.user_id, calculate_rating  FROM history_of_questions q WHERE q.user_id = %s AND q.calculate_rating = %s;",
            params=(user_id, False)
        )
    
    def get_all_histories(self, date, question_id):
        return super().get_many(
            query="SELECT q.id, q.hit_level, u.rating, u.rating_deviation, u.volatility FROM history_of_questions q JOIN history_of_user_rating_updates u ON q.history_of_user_rating_update_id = u.id WHERE q.answer_at >= %s AND q.question_id = %s",
            params=(date, question_id)
        )

    def create(self, id, create_at, question_id, user_id):
        return super().update(
            query="INSERT INTO history_of_questions (id, create_at, question_id, user_id, calculate_rating) VALUES (%s, %s, %s, %s, %s);",
            params=(id, create_at, question_id, user_id, False)
        )
        
    def insert_answer(self, id, answer_at, hit_level, time , user_id):
        return super().update(
            query="UPDATE history_of_questions SET answer_at = %s, hit_level = %s, time = %s WHERE id = %s AND user_id = %s;",
            params=(answer_at, hit_level, time, id, user_id)
        )
    
    def update_calculate_rating(self, id, user_id, calculate_rating, history_of_user_rating_update_id):
        return super().update(
            query="UPDATE history_of_questions SET calculate_rating = %s, history_of_user_rating_update_id = %s WHERE id = %s AND user_id = %s;",
            params=(calculate_rating,history_of_user_rating_update_id, id, user_id)
        )
    
    def get_question(self, id, user_id):
        return super().get_one(
            query="SELECT q.id, q.statement, q.answer, q.rating, q.is_essay, q.ability_id FROM questions q WHERE q.id = (SELECT question_id FROM history_of_questions WHERE id = %s and user_id = %s);",
            params=(id,user_id)
        )
    
    def get_question_id(self, id, user_id):
        return super().get_one(
            query="SELECT q.question_id FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;",
            params=(id,user_id)
        )    