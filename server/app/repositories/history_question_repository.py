
from app.domain.entities.history_of_question import HistoryOfQuestion
from app.domain.entities.question import Question
from app.domain.errors.api_exception import ApiException
from app.domain.errors.domain_errors import HistoryOfQuestionNotFound

class HistoryQuestionsRepository():
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_by_id(self, id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.create_at, q.answer_at, q.hit_level, q.time, q.question_id, q.user_id, q.calculate_rating  FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", (id,user_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, create_at, answer_at, hit_level, time, question_id, user_id, calculate_rating= cursor.fetchone()
        history_of_question = HistoryOfQuestion(id, create_at, answer_at, hit_level, time, question_id, user_id, calculate_rating)
        cursor.close()
        return history_of_question
    
    def get_history_without_answer(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.create_at, q.answer_at, q.hit_level, q.time, q.question_id, q.user_id, calculate_rating  FROM history_of_questions q WHERE q.user_id = %s AND q.answer_at IS NULL;", (user_id,))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, create_at, answer_at, hit_level, time, question_id, q_user_id, calculate_rating = cursor.fetchone()
        history_of_question = HistoryOfQuestion(id, create_at, answer_at, hit_level, time, question_id, q_user_id, calculate_rating )
        cursor.close()
        return history_of_question
    
    def get_all_history_without_calculate_rating(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.create_at, q.answer_at, q.hit_level, q.time, q.question_id, q.user_id, calculate_rating  FROM history_of_questions q WHERE q.user_id = %s AND q.calculate_rating = %s;", (user_id, False))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        histories_tuple = cursor.fetchall()
        histories = []
        for history_tuple in histories_tuple:            
            id, create_at, answer_at, hit_level, time, question_id, q_user_id, calculate_rating = history_tuple
            history_of_question = HistoryOfQuestion(id, create_at, answer_at, hit_level, time, question_id, q_user_id, calculate_rating )
            histories.append(history_of_question)
        cursor.close()
        return histories
    
    def get_all_histories(self, date, question_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.hit_level, u.rating, u.rating_deviation, u.volatility FROM history_of_questions q JOIN history_of_user_rating_updates u ON q.history_of_user_rating_update_id = u.id WHERE q.answer_at >= %s AND q.question_id = %s", (date, question_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        return cursor.fetchall()

    def create(self, id, create_at, question_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO history_of_questions (id, create_at, question_id, user_id, calculate_rating) VALUES (%s, %s, %s, %s, %s);", (id, create_at, question_id, user_id, False))
        cursor.close()
        
    def insert_answer(self, id, answer_at, hit_level, time , user_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE history_of_questions SET answer_at = %s, hit_level = %s, time = %s WHERE id = %s AND user_id = %s;", (answer_at, hit_level, time, id, user_id))
        cursor.close()
    
    def update_calculate_rating(self, id, user_id, calculate_rating, history_of_user_rating_update_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE history_of_questions SET calculate_rating = %s, history_of_user_rating_update_id = %s WHERE id = %s AND user_id = %s;", (calculate_rating,history_of_user_rating_update_id, id, user_id))
        cursor.close()
    
    def get_question(self, id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.statement, q.answer, q.rating, q.is_essay, q.ability_id FROM questions q WHERE q.id = (SELECT question_id FROM history_of_questions WHERE id = %s and user_id = %s);", (id,user_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, statement, answer, rating, is_essay, ability_id = cursor.fetchone()
        question = Question(id, statement, answer, is_essay, ability_id, rating= rating)
        cursor.close()
        return question
    
    def get_question_id(self, id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.question_id FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", (id,user_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        question_id = cursor.fetchone()
        cursor.close()
        return question_id
    
    
    
    
    