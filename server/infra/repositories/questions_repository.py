from domain.entities.question import Question
from domain.entities.alternatives import Alternatives
from infra.repositories.repository import Repository

class QuestionsRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_by_id(self, question_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.statement, q.answer, q.difficulty, q.is_essay FROM questions q WHERE q.id = %s;", (question_id,))
        id, statement, answer, difficulty, is_essay = cursor.fetchone()
        question = Question(id, statement, answer, difficulty, is_essay)
        cursor.execute("SELECT a.id, a.text FROM alternatives a WHERE a.question_id = %s;", (question_id,))
        alternatives_tuple = cursor.fetchall()
        templist = [] 
        for alternative_tuple in alternatives_tuple:
            alternative_id, alternative_text = alternative_tuple
            templist.append(Alternatives(alternative_id, alternative_text))
        list_sorted = sorted(templist, key = lambda obj: obj.id)
        question.add_list_alternative(list_sorted)
        cursor.close()
        return question
    
    