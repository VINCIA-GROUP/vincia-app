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
      if (history_mock_exam != None and history_mock_exam.is_open == True):
         return {"questions": self.deserialize(history_mock_exam.questions), 
                 "answers": self.deserialize(history_mock_exam.answers), 
                 "durations": self.deserialize(history_mock_exam.durations),
                 "ratings": self.deserialize(history_mock_exam.ratings),
                 "correctAnswers": self.deserialize(history_mock_exam.correct_answers)}
      else:
         questions = (
            self.get_areas_questions(AreasID.LANGUAGES.value, 815, 1462) + 
            self.get_areas_questions(AreasID.HUMANITIES.value, 1000, 1500) + 
            self.get_areas_questions(AreasID.NATURAL_SCIENCE.value, 1000, 1500) + 
            self.get_areas_questions(AreasID.MATHEMATICS.value, 1350, 1750)
         )
         answers = [""] * 180
         durations = [0] * 180
         ratings = [0] * 180
         correct_answers = [""] * 180
         history_id = str(uuid.uuid4())
         self.history_of_mock_exam_repository.create_exam(history_id, questions, answers, durations, ratings, correct_answers, user_id)
         self.history_of_mock_exam_repository.commit()
         return {"questions": questions, 
                 "answers": answers, 
                 "durations": durations, 
                 "ratings": ratings,
                 "correctAnswers": correct_answers}

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
      
   def submit_answer(self, user_id, answers, durations, ratings, correct_answers):
      self.history_of_mock_exam_repository.update_exam(
         answers,
         durations,
         ratings,
         correct_answers,
         user_id
      )
      self.history_of_mock_exam_repository.commit()

   def submmit(self, user_id):
      None
      # hit = []
      # mock_exam = self.history_of_mock_exam_repository.get_by_user_id(user_id)
      # for questionId in mock_exam.questions:
      #    question = self.question_repository.get_by_id(questionId)


      # self.history_of_questions_repository.finish_exam(
      #    user_id,
      #    languages_grade, 
      #    humanities_grade, 
      #    mathematics_grade, 
      #    natural_science_grade, 
      #    general_grade, 
      #    False   
      # )
      # self.history_of_mock_exam_repository.commit()

   def get_grade(self, questions, anwers, correct_answers, answers):
      None

   def deserialize(self, input_string):
      input_string = input_string.strip("{}")
      items = input_string.split(",")
      result_list = []
      for item in items:
         item = item.strip() 
         if item == '""':
               result_list.append("")
         else:
               result_list.append(item)
      return result_list