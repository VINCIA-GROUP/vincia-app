import random
from app.domain.enums.areas_id import AreasID

class MockExamService:

   def __init__(self, question_repository, history_of_questions_repository):
      self.question_repository = question_repository
      self.history_of_questions_repository = history_of_questions_repository

   def get_mock_exam_questions(self): #90 questoes
      questions = [[], [], [], []]
      for areaIndex, area in enumerate(AreasID):
         questions[areaIndex] = self.get_areas_questions(area.value)
      return questions

   def get_areas_questions(self, area): #45 questoes  11 facil / 23 normal / 11 dificil
      questions = []
      easy_questions = self.question_repository.get_by_area_and_difficult(area, 0, 1000)
      list(map(lambda question: questions.append(question), self.choose_questions(easy_questions, 11)))
      normal_questions = self.question_repository.get_by_area_and_difficult(area, 1000, 1500)
      list(map(lambda question: questions.append(question), self.choose_questions(normal_questions, 23)))
      hard_questions = self.question_repository.get_by_area_and_difficult(area, 1500, 9999)
      list(map(lambda question: questions.append(question), self.choose_questions(hard_questions, 11)))
      if (len(easy_questions) == 0 or len(normal_questions) == 0 or len(hard_questions) == 0):
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
   
   # def submit_answer(self, user_id, answers):
   #    for answer in answers:
         

   # def calculate_grade():