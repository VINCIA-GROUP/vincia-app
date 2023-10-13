from datetime import datetime
from app.domain.entities.history_of_mock_exam import History_of_Mock_exam
from app.repositories.repository import Repository

class HistoryOfMockExamRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, History_of_Mock_exam)

   def get_all(self):
      return super().get_many(query="SELECT * FROM history_of_mock_exam;", params="")
      
   def get_by_id(self, id):
      return super().get_one(
         query="SELECT * FROM history_of_mock_exam q WHERE q.id = %s;", params=(id,))
   
   def get_by_user_id(self, user_id):
      return super().get_one(
         query="SELECT * FROM history_of_mock_exam exam WHERE exam.user_id = %s ORDER BY exam.created_at DESC LIMIT 1;", 
         params=(user_id,))
      
   def get_last(self):
      return super().get_one(
         query="SELECT * FROM history_of_mock_exam ORDER BY date_column DESC LIMIT 1;", params="")
   
   def create_exam(self, id, questions, answers, durations, user_id):
      return super().update(
         query="INSERT INTO history_of_mock_exam (id, user_id, created_at, questions, answers, durations, is_open) VALUES (%s, %s, %s, %s, %s, %s, %s);",
         params=(id, user_id, datetime.utcnow(), questions, answers, durations, True),)
   
   def update_exam(self, id, questions, answers, durations, user_id, is_open):
      return super().update(
         query="INSERT INTO history_of_mock_exam (id, user_id, questions, answers, durations, is_open) VALUES (%s, %s, %s, %s, %s);",
         params=(id, user_id, questions, answers, durations, is_open),)