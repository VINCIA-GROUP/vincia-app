from domain.entities.question import Question
from domain.entities.alternatives import Alternatives
from infra.repositories.repository import Repository

class QuestionsRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_by_id(self, question_id):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.statement, q.answer, q.rating, q.rating_deviation, q.volatility, q.last_rating_update, q.is_essay FROM questions q WHERE q.id = %s;", (question_id,))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        id, statement, answer, rating, rating_deviation, volatility, last_rating_update, is_essay = cursor.fetchone()
        question = Question(id, statement, answer, is_essay, rating, rating_deviation, volatility, last_rating_update)
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
    
    def get_question_by_rating(self, rating, limit):
        cursor = self.conn.cursor()
        cursor.execute("SELECT q.id, q.statement, q.answer, q.rating, q.rating_deviation, q.volatility, q.last_rating_update, q.is_essay FROM questions q WHERE rating BETWEEN 0 AND (SELECT MAX(rating) FROM questions) ORDER BY ABS(q.rating - %s) LIMIT %s;", (rating, limit))
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        questions_tuple = cursor.fetchall()
        list_questions = []
        for question_tuple in questions_tuple:
            question_id, question_statement, question_answer, question_rating, question_rating_deviation, question_volatility, question_last_rating_update, question_is_essay = question_tuple
            question = Question(question_id, question_statement, question_answer, question_is_essay, rating= question_rating, rating_deviation= question_rating_deviation, volatility= question_volatility, last_rating_update= question_last_rating_update)
            cursor.execute("SELECT a.id, a.text FROM alternatives a WHERE a.question_id = %s;", (question_id,))
            alternatives_tuple = cursor.fetchall()
            templist = [] 
            for alternative_tuple in alternatives_tuple:
                alternative_id, alternative_text = alternative_tuple
                templist.append(Alternatives(alternative_id, alternative_text))
            list_sorted = sorted(templist, key = lambda obj: obj.id)
            question.add_list_alternative(list_sorted)
            list_questions.append(question)
        cursor.close()
        return list_questions