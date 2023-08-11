from app.domain.entities.question import Question
from app.repositories.repository import Repository
from app.repositories.alternatives_repository import AlternativeRepository

class QuestionsRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, Question)

   def get_all(self):
      alternatives_repository = AlternativeRepository(self.connection)
      query = "SELECT * FROM questions;"
      questions = super().get_many(query=query, params="")
      for question in questions:
         question.alternatives = alternatives_repository.get_by_question(question)
      return questions

   def get_by_id(self, id):
      alternatives_repositories = AlternativeRepository(self.connection)
      query = "SELECT * FROM questions q WHERE q.id = %s;"
      question = super().get_one(query=query, params=(id,))
      question.alternatives = alternatives_repositories.get_by_question(question)
      return question

   def get_filtered(self, filters): #filter_example = {"rating": "> 1.0", "is_essay": "= false"}
      alternatives_repository = AlternativeRepository(self.connection)
      if filters:
         conditions = []
         query = "SELECT * FROM questions q WHERE "
         for column, filter in filters.items():
            condition = f"{column} {filter}"
            conditions.append(condition)
         query += " AND ".join(conditions)
         query += ";"
      questions = super().get_many(query=query, params="")
      for question in questions:
         question.alternatives = alternatives_repository.get_alternatives_by_question(question)
      return questions
   
   def get_by_rating(self, rating, limit, ability_id):
      alternatives_repository = AlternativeRepository(self.connection)
      query = "SELECT * FROM questions q WHERE ability_id = %s AND rating BETWEEN 0 AND (SELECT MAX(rating) FROM questions) ORDER BY ABS(q.rating - %s) LIMIT %s;"
      params = (ability_id,rating, limit)
      questions = super().get_many(query=query, params=params)
      for question in questions:
         question.alternatives = alternatives_repository.get_by_question(question)
      return questions
   
   def get_by_area_and_difficult(self, area_id, rating_low, rating_high):
      alternatives_repository = AlternativeRepository(self.connection)
      query = "SELECT q.* FROM questions q JOIN abilities a ON q.ability_id = a.id WHERE q.is_essay = false AND a.area_id = %s AND rating BETWEEN %s AND %s;"
      params = (area_id, rating_low, rating_high)
      questions = super().get_many(query=query, params=params)
      for question in questions:
         question.alternatives = alternatives_repository.get_by_question(question)
      return questions

   def update_rating(self, id, rating, rating_deviation, volatility):
      query = "UPDATE questions SET rating = %s, rating_deviation = %s, volatility = %s WHERE id = %s;"
      params = (rating, rating_deviation, volatility, id)
      result = super().update(query=query, params=params)
      return result