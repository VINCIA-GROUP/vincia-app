from app.domain.entities.history_of_question import HistoryOfQuestion
from app.repositories.repository import Repository

class HistoryOfQuestionRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, HistoryOfQuestion)  

   def get_by_id(self, id, user_id):
      return super().get_one(
         query="SELECT * FROM history_of_questions q WHERE q.id = %s AND q.user_id = %s;", 
         params=(id,user_id)
      )
   
   def get_history_without_answer(self, user_id):
      return super().get_many(
         query="SELECT * FROM history_of_questions q WHERE q.user_id = %s AND q.answer_at IS NULL;",
         params=(user_id,)
      ) 