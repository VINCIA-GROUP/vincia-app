from psycopg2 import DatabaseError
from app.domain.entities.alternatives import Alternative

class AlternativeRepository:

   def __init__(self, connection):
      self.connection = connection

   def get_by_question(self, question):
      alternatives = []
      try:
         cursor = self.connection.cursor()
         cursor.execute(
             "SELECT * FROM alternatives a WHERE a.question_id = %s;", (question.id,))
         rows = self.cursor.fetchall()
         for row in rows:
            alternatives.append(Alternative(*row))
         cursor.close()
      except DatabaseError as error:
         print('AlternativeRepository - get_by_question - ' + error)
      return alternatives

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