from psycopg2 import DatabaseError
from app.domain.entities.question import Question
from app.repositories.alternatives_repository import AlternativeRepository

class QuestionsRepository:
   def __init__(self, connection):
      self.connection = connection

   def get_all(self):
      questions = []
      alternatives_repository = AlternativeRepository(self.connection)
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM questions;")
         rows = cursor.fetchall()
         for row in rows:
            question = Question(*row)
            alternatives = alternatives_repository.get_alternatives_by_question(question)
            question.alternatives = alternatives
            questions.append(question)
         cursor.close()
      except DatabaseError as error:
         print('QuestionsRepository - get_all - ' + error)
      return questions

   def get_by_id(self, id):
      question = Question()
      alternatives_repositories = AlternativeRepository(self.connection)
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM questions q WHERE q.id = %s;", (id,))
         row = cursor.fetchone()
         question = Question(*row)
         alternatives = alternatives_repositories.get_alternatives_by_question(question)
         question.alternatives = alternatives
      except DatabaseError as error:
         print('QuestionsRepository - get_by_id - ' + error)
      return question

   def get_filtered(self, filters): #filter_example = {"rating": "> 1.0", "is_essay": "= false"}
      questions = []
      conditions = []
      alternatives_repository = AlternativeRepository(self.connection)
      try:
         cursor = self.connection.cursor()
         if filters:
            query = "SELECT * FROM questions q WHERE "
            for column, filter in filters.items():
               condition = f"{column} {filter}"
               conditions.append(condition)
            query += " AND ".join(condition)
            query += ";"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
               question = Question(*row)
               alternatives = alternatives_repository.get_alternatives_by_question(question)
               question.alternatives(alternatives)
               questions.append(question)
         else:
            questions = self.get_all()
      except DatabaseError as error:
         print('QuestionsRepository - get_filtered - ' + error)
      return questions
   
   def update_rating(self, id, rating, rating_deviation, volatility):
      try:
         cursor = self.connection.cursor()
         cursor.execute("UPDATE questions SET rating = %s, rating_deviation = %s, volatility = %s WHERE id = %s;", (rating, rating_deviation, volatility, id))
         cursor.close
         return True
      except DatabaseError as error:
         print('QuestionsRepository - update_rating - ' + error)
         return False
      
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