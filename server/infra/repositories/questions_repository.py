import psycopg2
import os
from domain.entities.question import Question
from domain.entities.alternatives import Alternatives

class QuestionsRepository:
    def __init__(self):    
        sc = os.environ["CONNECTION_STRING_DB"]    
        self.conn = psycopg2.connect(sc)
        
    def get_question(self, question_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.statement, q.answer, q.difficulty, q.is_essay FROM questions q WHERE q.id = %s;", (question_id,))
        id, statement, answer, difficulty, is_essay = cursor.fetchone()
        question = Question(id, statement, answer, difficulty, is_essay)
        cursor.execute("SELECT a.id, a.text FROM alternatives a;")
        alternatives_tuple = cursor.fetchall()
        for alternative_tuple in alternatives_tuple:
            alternative_id, alternative_text = alternative_tuple
            question.add_alternative(Alternatives(alternative_id, alternative_text))
        
        return question