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
      
   def create_exam(self, id, questions, answers, durations, ratings, correct_answers, user_id):
      super().update(
         query="INSERT INTO history_of_mock_exam (id, user_id, created_at, questions, answers, durations, ratings, correct_answers, is_open) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
         params=(id, user_id, datetime.utcnow(), questions, answers, durations, ratings, correct_answers, True,))
   
   def update_exam(self, answers, durations, ratings, correct_answers, user_id):
      super().update(
         query="UPDATE history_of_mock_exam SET answers = %s, durations = %s, ratings = %s, correct_answers = %s WHERE user_id = %s AND created_at = (SELECT MAX (created_at) FROM history_of_mock_exam WHERE user_id = %s)",
         params=(answers, durations, ratings, correct_answers, user_id, user_id,))
   
   def finish_exam(self, user_id, languages_grade, humanities_grade, mathematics_grade, natural_science_grade, general_grade, is_open):
      super().update(
         query="UPDATE history_of_mock_exam SET languages_grade = %s, humanities_grade = %s, mathematics_grade = %s, natural_science_grade = %s, general_grade = %s, is_open = %s WHERE user_id = %s AND created_at = (SELECT MAX (created_at) FROM history_of_mock_exam WHERE user_id = %s",
         params=(languages_grade, humanities_grade, mathematics_grade, natural_science_grade, general_grade, is_open, user_id, user_id,))
