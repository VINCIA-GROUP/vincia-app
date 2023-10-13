import uuid
import random
from app.domain.enums.areas_id import AreasID

class MockExamService:

   def __init__(self, question_repository, history_of_questions_repository, history_of_mock_exam_repository):
      self.question_repository = question_repository
      self.history_of_questions_repository = history_of_questions_repository
      self.history_of_mock_exam_repository = history_of_mock_exam_repository

   def get_mock_exam_questions(self, user_id): #180 questoes
      history_mock_exam = self.history_of_mock_exam_repository.get_by_user_id(user_id)
      if (history_mock_exam != None and history_mock_exam.is_open == "true"):
         return {"questions": history_mock_exam.questions, "answers": history_mock_exam.answers, "durations": history_mock_exam.durations}
      else:
         questions = (
            self.get_areas_questions(AreasID.LANGUAGES.value, 815, 1462) + 
            self.get_areas_questions(AreasID.HUMANITIES.value, 1000, 1500) + 
            self.get_areas_questions(AreasID.NATURAL_SCIENCE.value, 1000, 1500) + 
            self.get_areas_questions(AreasID.MATHEMATICS.value, 1350, 1750)
         )
         answers = [None] * 180
         durations = [None] * 180
         history_id = str(uuid.uuid4())
         self.history_of_mock_exam_repository.create_exam(history_id, questions, answers, durations, user_id)
         return {"questions": questions, "answers": answers, "durations": durations}

   def get_areas_questions(self, area, rating_low, rating_high): #45 questoes  11 facil / 23 normal / 11 dificil
      questions = []
      list(map(lambda question: questions.append(question),
         self.question_repository.get_random_by_difficult(area, 0, rating_low, 11)))
      list(map(lambda question: questions.append(question),
         self.question_repository.get_random_by_difficult(area, rating_low, rating_high, 23)))
      list(map(lambda question: questions.append(question),
         self.question_repository.get_random_by_difficult(area, rating_high, 9999, 11)))
      if (len(questions) < 45):
         return []
      random.shuffle(questions)
      return questions
   
   def get_question(self, id):
      question = self.question_repository.get_by_id(id)
      return question.to_json()
      
   def submit_answer(self, user_id, answers):
      for answer in answers:
         None#save answer in database

   def calculate_grade():
      None