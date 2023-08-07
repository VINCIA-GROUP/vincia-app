from app.domain.enums.areas_id import AreasID

class MockExamService:

   def __init__(self, question_repository):
      self.question_repository = question_repository

   def get_mock_exam_questions(self): #90 questoes
      questions = []
      natural_science = self.get_areas_questions(AreasID.NATURAL_SCIENCE)
      humanities = self.get_areas_questions(AreasID.HUMANITIES)
      languages = self.get_areas_questions(AreasID.LANGUAGES)
      mathematics = self.get_areas_questions(AreasID.MATHEMATICS)
      if (len(natural_science) == 0 | len(natural_science) == 0 | len(natural_science) == 0 | len(natural_science) == 0):
         return []
      else:
         questions.append(natural_science)
         questions.append(humanities)
         questions.append(languages)
         questions.append(mathematics)
      return questions

   def get_areas_questions(self, area): #45 questoes  11 facil / 23 normal / 11 dificil
      questions = []
      easy_questions = self.filter_questions(area, "easy")
      normal_questions = self.filter_questions(area, "normal")
      hard_questions = self.filter_questions(area, "hard")
      if (len(easy_questions) == 0 | len(normal_questions) == 0 | len(hard_questions) == 0):
         return []
      else:
         questions.append(self.choose_questions(easy_questions, 11))
         questions.append(self.choose_questions(normal_questions, 23))
         questions.append(self.choose_questions(hard_questions, 11))
      return questions

   def filter_questions(self, area_id, difficulty): # dissertativas / dificuldade / area
      rating = "BETWEEN 0.8 AND 1.2"
      rating = "< 0.8" if difficulty == "easy" else rating
      rating = "> 1.5" if difficulty == "hard" else rating
      filters = {"area_id": area_id, "rating": rating, "is_essay": "= false", }
      questions = self.question_repository.get_filtered(filters)
      return questions
   
   def choose_questions(self, questions, amount): #distribuir as questões pelas habilidades
      chosen_questions = []
      abilities = [question.ability_id() for question in questions]
      abilities.sort()
      count_ability = {}
      for ability in abilities:
         if ability in count_ability:
            count_ability[ability] += 1
         else:
            count_ability[ability] = 1
      
      #dividir a mesma quantidade pra cada e distribuir  
      return chosen_questions


