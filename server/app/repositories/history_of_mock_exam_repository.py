from app.domain.entities.history_of_mock_exam import History_of_Mock_exam
from app.repositories.repository import Repository

class HistoryOfMockExamRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, History_of_Mock_exam)

   def get_all(self):
      return super().get_many(query="SELECT * FROM questions;", params="")
      
   def get_by_id(self, id):
      return super().get_one(
         query="SELECT * FROM questions q WHERE q.id = %s;", params=(id,))
      
   def get_last(self):
      return super().get_one(
         query="SELECT * FROM sua_tabela ORDER BY date_column DESC LIMIT 1;", params="")