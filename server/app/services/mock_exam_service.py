import random
from app.domain.enums.areas_id import AreasID

class MockExamService:

   def __init__(self, question_repository):
      self.question_repository = question_repository

   def get_mock_exam_questions(self): #90 questoes
      questions = []
      natural_science = self.get_areas_questions(AreasID.NATURAL_SCIENCE.value)
      humanities = self.get_areas_questions(AreasID.HUMANITIES.value)
      languages = self.get_areas_questions(AreasID.LANGUAGES.value)
      mathematics = self.get_areas_questions(AreasID.MATHEMATICS.value)
      if (len(natural_science) == 0 or len(natural_science) == 0 or len(natural_science) == 0 or len(natural_science) == 0):
         return []
      else:
         questions.append(natural_science)
         questions.append(humanities)
         questions.append(languages)
         questions.append(mathematics)
      return questions

   def get_areas_questions(self, area): #45 questoes  11 facil / 23 normal / 11 dificil
      questions = []
      easy_questions = self.question_repository.get_by_area_and_difficult(area, 0, 700)
      normal_questions = self.question_repository.get_by_area_and_difficult(area, 700, 1500)
      hard_questions = self.question_repository.get_by_area_and_difficult(area, 1500, 9999)
      if (len(easy_questions) == 0 or len(normal_questions) == 0 or len(hard_questions) == 0):
         return []
      else:
         questions.append(self.choose_questions(easy_questions, 11))
         questions.append(self.choose_questions(normal_questions, 23))
         questions.append(self.choose_questions(hard_questions, 11))
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
            random_question_index = random.randint(0, len(value)-1) if len(value) > 0 else 0
            chosen_questions.append(value[random_question_index])
            abilities[key].pop(random_question_index)
      return chosen_questions