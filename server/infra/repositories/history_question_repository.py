
from domain.entities.history_of_question import HistoryOfQuestion
from domain.errors.api_exception import ApiException
from domain.errors.domain_errors import HistoryOfQuestionNotFound
from infra.repositories.repository import Repository

class HistoryQuestionsRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_by_id(self, id, user_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.date, q.hit_level, q.var_grade, q.time, q.question_id FROM history_of_questions q WHERE q.id = %s and q.user_id = %s;", (id,user_id))
        if(cursor.rowcount <= 0):
            cursor.close()
            raise ApiException(HistoryOfQuestionNotFound())
        id, date, hit_level, var_grade, time, question_id = cursor.fetchone()
        question = HistoryOfQuestion(id, date, hit_level, var_grade, time, question_id, user_id)
        cursor.close()
        return question
    
    