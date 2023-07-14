
from domain.entities.history_of_question import HistoryOfQuestion
from domain.entities.question import Question
from domain.errors.api_exception import ApiException
from domain.errors.domain_errors import HistoryOfQuestionNotFound
from infra.repositories.repository import Repository

class HistoryQuestionsRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_by_id(self, id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.create_at, q.answer_at, q.hit_level, q.time, q.question_id, q.user_id FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", (id,user_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, create_at, answer_at, hit_level, time, question_id, user_id= cursor.fetchone()
        history_of_question = HistoryOfQuestion(id, create_at, answer_at, hit_level, time, question_id, user_id)
        cursor.close()
        return history_of_question
    
    def get_history_without_answer(self, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.create_at, q.answer_at, q.hit_level, q.time, q.question_id, q.user_id FROM history_of_questions q WHERE q.user_id = %s AND q.answer_at IS NULL;", (user_id,))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, create_at, answer_at, hit_level, time, question_id, q_user_id= cursor.fetchone()
        history_of_question = HistoryOfQuestion(id, create_at, answer_at, hit_level, time, question_id, q_user_id)
        cursor.close()
        return history_of_question
    
    def create(self, id, create_at, question_id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO history_of_questions (id, create_at, question_id, user_id) VALUES (%s, %s, %s, %s);", (id, create_at, question_id, user_id))
        cursor.close()
        
    def insert_answer(self, id, answer_at, hit_level, time , user_id):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE history_of_questions SET answer_at = %s, hit_level = %s, time = %s WHERE id = %s AND user_id = %s;", (answer_at, hit_level, time, id, user_id))
        cursor.close()
    
    def get_question(self, id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.statement, q.answer, q.rating, q.is_essay FROM questions q WHERE q.id = (SELECT question_id FROM history_of_questions WHERE id = %s and user_id = %s);", (id,user_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, statement, answer, rating, is_essay = cursor.fetchone()
        question = Question(id, statement, answer, is_essay, rating= rating)
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
    
    