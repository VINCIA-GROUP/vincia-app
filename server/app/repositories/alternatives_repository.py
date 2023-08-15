from app.repositories.repository import Repository
from app.domain.entities.alternatives import Alternative

class AlternativeRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, Alternative)

   def get_by_question(self, question):
      return super().get_many(
         query="SELECT id, text, question_id FROM alternatives WHERE question_id = %s;",
         params=(question.id,))
