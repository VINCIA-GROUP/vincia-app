from app.domain.entities.history_of_question import HistoryOfQuestion
from app.domain.entities.question import Question
from app.repositories.repository import Repository

class HistoryOfQuestionsRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, HistoryOfQuestion)  

   def get_by_id(self, id, user_id):
      return super().get_one(
         query="SELECT q.id, q.create_at, q.hit_level, q.time, q.question_id, q.history_of_user_rating_update_id, q.user_id FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", 
         params=(id,user_id)
      )
   
   def get_all_abilities_history_without_rating_id(self, user_id):
      cursor = self.connection.cursor()
      cursor.execute("SELECT DISTINCT qt.ability_id FROM history_of_questions q JOIN questions qt ON q.question_id = qt.id WHERE q.user_id = %s AND q.history_of_user_rating_update_id IS NULL;" , (user_id, ))
      if(cursor.rowcount <= 0):
         cursor.close()
         return None
      result = cursor.fetchall()
      cursor.close()
      return result
   
   def get_all_history_without_rating_id(self, user_id, ability_id, date):
      return super().get_many(
         query="SELECT h.id, h.create_at, h.hit_level, h.time, h.question_id, h.history_of_user_rating_update_id, h.user_id  FROM history_of_questions h JOIN questions q ON h.question_id = q.id WHERE h.history_of_user_rating_update_id IS NULL AND h.user_id = %s AND q.ability_id = %s AND h.create_at = %s;",
         params=(user_id, ability_id, date)
      )
   
   def get_all_histories(self, date, question_id):
      cursor = self.connection.cursor()
      cursor.execute("SELECT q.id, q.hit_level, u.rating, u.rating_deviation, u.volatility FROM history_of_questions q JOIN history_of_user_rating_updates u ON q.history_of_user_rating_update_id = u.id WHERE q.create_at >= %s AND q.question_id = %s", (date, question_id))
      if(cursor.rowcount <= 0):
         cursor.close()
         return None
      result = cursor.fetchall()
      cursor.close()
      return result
   
   def get_last_abilities_use(self, quantity, user_id):
      cursor = self.connection.cursor()
      cursor.execute("SELECT DISTINCT ar.id, hq.create_at FROM history_of_questions hq JOIN questions q ON q.id = hq.question_id JOIN abilities a ON a.id = q.ability_id JOIN abilities_rating ar ON ar.ability_id = a.id WHERE ar.user_id = %s AND hq.user_id = %s ORDER BY hq.create_at LIMIT %s", (user_id, user_id, quantity))
      if(cursor.rowcount <= 0):
         cursor.close()
         return None
      result = cursor.fetchall()
      cursor.close()
      return result
      

   def create(self, id, create_at, hit_level, duration, question_id, user_id):
      super().update(
         query="INSERT INTO history_of_questions (id, create_at, hit_level, time, question_id, user_id) VALUES (%s, %s, %s, %s, %s, %s);",
         params=(id, create_at,hit_level, duration, question_id, user_id)
      )

   
   def update_rating(self, id, user_id, history_of_user_rating_update_id):
      super().update(
         query="UPDATE history_of_questions SET history_of_user_rating_update_id = %s WHERE id = %s AND user_id = %s;",
         params=(history_of_user_rating_update_id, id, user_id)
      )
    
   def get_question_id(self, id, user_id):
      cursor = self.connection.cursor()
      cursor.execute("SELECT q.question_id FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", (id,user_id))
      if(cursor.rowcount <= 0):
         cursor.close()
         return None
      question_id = cursor.fetchone()
      cursor.close()
      return question_id
   