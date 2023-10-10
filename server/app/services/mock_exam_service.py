import random
from app.domain.enums.areas_id import AreasID

class MockExamService:

   def __init__(self, question_repository, history_of_questions_repository, history_of_mock_exam_repository):
      self.question_repository = question_repository
      self.history_of_questions_repository = history_of_questions_repository
      self.history_of_mock_exam_repository = history_of_mock_exam_repository

   def get_mock_exam_questions(self): #90 questoes
      questions = [[], [], [], []]
      questions[0] = self.get_areas_questions(AreasID.LANGUAGES.value, 815, 1462)
      questions[1] = self.get_areas_questions(AreasID.HUMANITIES.value, 1000, 1500)
      questions[2] = self.get_areas_questions(AreasID.NATURAL_SCIENCE.value, 1000, 1500)
      questions[3] = self.get_areas_questions(AreasID.MATHEMATICS.value, 1350, 1750)
      return questions

   def get_areas_questions(self, area, rating_low, rating_high): #45 questoes  11 facil / 23 normal / 11 dificil
      questions = []
      list(map(lambda question: questions.append(question.to_json()),
         self.question_repository.get_random_by_difficult(area, 0, rating_low, 11)))
      list(map(lambda question: questions.append(question.to_json()),
         self.question_repository.get_random_by_difficult(area, rating_low, rating_high, 23)))
      list(map(lambda question: questions.append(question.to_json()),
         self.question_repository.get_random_by_difficult(area, rating_high, 9999, 11)))
      if (len(questions) < 45):
         return []
      return questions
   
   def choose_questions(self, questions, amount): #distribuir as questões pelas habilidades
      chosen_questions = []
      abilities = {}
      for question in questions:
         if question.ability_id in abilities:
            abilities[question.ability_id].append(question)
         else:
            abilities[question.ability_id] = [question]
      while len(chosen_questions) < amount:
         for key, value in abilities.items():
            if (len(value) > 0):
               random_question_index = random.randint(0, len(value)-1) if len(value) > 1 else 0
               chosen_questions.append(value[random_question_index].to_json())
               abilities[key].pop(random_question_index)
      return chosen_questions
   
   def submit_answer(self, user_id, answers):
      for answer in answers:
         None#save answer in database
         

   def calculate_grade():
      None