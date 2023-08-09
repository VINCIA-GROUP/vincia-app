from psycopg2 import DatabaseError
from app.domain.entities.history_of_question import HistoryOfQuestion

class HistoryOfQuestionRepository():
   def __init__(self, connection):
      self.connection = connection

   def get_by_id(self, id, user_id):
      history = HistoryOfQuestion()
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", (id,user_id))
         row = cursor.fetchone()
         history = HistoryOfQuestion(*row)
         cursor.close()
      except DatabaseError as error:
         print('HistoryOfQuestionRepository - get_by_id - ' + error)
      return history 
   
   def get_history_without_answer(self, user_id):
      history_of_questions = []
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM history_of_questions q WHERE q.user_id = %s AND q.answer_at IS NULL;", (user_id,))
         rows = cursor.fetchall()
         for row in rows:
            history = HistoryOfQuestion(*row)
            history_of_questions.append(history)
         cursor.close()
      except DatabaseError as error:
         print('HistoryOfQuestionRepository - get_history_without_answer - ' + error)
      return history_of_questions

   

   def commit(self):
      try:
         self.connection.commit()
         return True
      except DatabaseError as error:
         print('QuestionsRepository - commit - ' + error)
         return False
      
   def rollback(self):
      try:
         self.connection.rollback()
         return True
      except DatabaseError as error:
         print('QuestionsRepository - rollback - ' + error)
         return False
