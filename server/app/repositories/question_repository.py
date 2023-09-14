from app.domain.entities.alternatives import Alternative
from app.domain.entities.question import Question
from app.repositories.repository import Repository

class QuestionsRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, Question)

   def get_all(self):
      questions = super().get_many(query="SELECT q.id, q.statement, q.answer, q.is_essay, q.ability_id, q.rating, q.rating_deviation, q.volatility, q.last_rating_update  FROM questions;", params="")
      for question in questions:
         question.alternatives = self._get_alternatives(question.id)
      return questions

   def get_by_id(self, id):
      question = super().get_one(
         query="SELECT q.id, q.statement, q.answer, q.is_essay, q.ability_id, q.rating, q.rating_deviation, q.volatility, q.last_rating_update FROM questions q WHERE q.id = %s;", params=(id,))
      question.alternatives = self._get_alternatives(question.id)
      return question
   
   def get_by_id_without_alternatives(self, id):
      question = super().get_one(
         query="SELECT q.id, q.statement, q.answer, q.is_essay, q.ability_id, q.rating, q.rating_deviation, q.volatility, q.last_rating_update FROM questions q WHERE q.id = %s;", params=(id,))
      return question
   
   def get_date_last_update(self, id):
      cursor = self.connection.cursor()
      cursor.execute("SELECT last_rating_update FROM questions WHERE id = %s" , (id,))
      if(cursor.rowcount <= 0):
         cursor.close()
         return None
      result, = cursor.fetchone()
      cursor.close()
      return result

   def get_filtered(self, filters): #filter_example = {"rating": "> 1.0", "is_essay": "= false"}
      if filters:
         conditions = []
         query = "SELECT q.id, q.statement, q.answer, q.is_essay, q.ability_id, q.rating, q.rating_deviation, q.volatility, q.last_rating_update  FROM questions q WHERE "
         for column, filter in filters.items():
            condition = f"{column} {filter}"
            conditions.append(condition)
         query += " AND ".join(conditions)
         query += ";"
      questions = super().get_many(query=query, params="")
      for question in questions:
         question.alternatives = self._get_alternatives(question.id)
      return questions
   
   def get_by_rating(self, rating, limit, ability_id):
      questions = super().get_many(
         query="SELECT q.id, q.statement, q.answer, q.is_essay, q.ability_id, q.rating, q.rating_deviation, q.volatility, q.last_rating_update FROM questions q WHERE ability_id = %s AND rating BETWEEN 0 AND (SELECT MAX(rating) FROM questions) ORDER BY ABS(q.rating - %s) LIMIT %s;", 
         params=(ability_id,rating, limit)
      )
      for question in questions:
         question.alternatives = self._get_alternatives(question.id)
      return questions
   
   def get_by_area_and_difficult(self, area_id, rating_low, rating_high):
      questions = super().get_many(
         query="SELECT q.id, q.statement, q.answer, q.is_essay, q.ability_id, q.rating, q.rating_deviation, q.volatility, q.last_rating_update  FROM questions q JOIN abilities a ON q.ability_id = a.id WHERE q.is_essay = false AND a.area_id = %s AND rating BETWEEN %s AND %s;", 
         params=(area_id, rating_low, rating_high)
      )
      for question in questions:
         question.alternatives = self._get_alternatives(question.id)
      return questions

   def update_rating(self, id, rating, rating_deviation, volatility, last_rating_update):
      return super().update(
         query="UPDATE questions SET rating = %s, rating_deviation = %s, volatility = %s, last_rating_update = %s WHERE id = %s;", 
         params=(rating, rating_deviation, volatility, last_rating_update, id)
      )

   def _get_alternatives(self, question_id):
      cursor = self.connection.cursor()
      cursor.execute("SELECT a.id, a.text FROM alternatives a WHERE a.question_id = %s;", (question_id,))
      alternatives_tuple = cursor.fetchall()
      templist = [] 
      for alternative_tuple in alternatives_tuple:
         alternative_id, alternative_text = alternative_tuple
         templist.append(Alternative(alternative_id, alternative_text))
      list_sorted = sorted(templist, key = lambda obj: obj.id)
      cursor.close()
      return list_sorted