from app.domain.entities.adaptive_question_selection import AdaptiveQuestionSelection
from app.repositories.repository import Repository

class AdaptiveQuestionSelectionRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, AdaptiveQuestionSelection)  
   
   def insert(self, entity):
      super().update(
               query="INSERT INTO adaptive_question_selection (id, create_at, question_id, user_id) VALUES (%s, %s, %s, %s);",
               params=(entity.id, entity.create_at, entity.question_id, entity.user_id)
         )
      
   def get_any(self, user_id):
      return super().get_one(
         query="SELECT id, create_at, question_id, user_id FROM adaptive_question_selection WHERE user_id = %s;", 
         params=(user_id,)
      )
      
   def remove_by_id(self, id, user_id):
      return super().update(
         query="DELETE FROM adaptive_question_selection WHERE id = %s AND user_id = %s;", 
         params=(id,user_id)
      )