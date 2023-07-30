from app.dao.question_dao import QuestionDAO
from app.models.question import Question
from typing import List
from enums import AreasID

class MockExamService():

   def get_mock_exam_questions(self): #90 questoes
      questions = []
      questions.append(self.get_areas_questions(AreasID.NATURAL_SCIENCE))
      questions.append(self.get_areas_questions(AreasID.HUMANITIES))
      questions.append(self.get_areas_questions(AreasID.LANGUAGES))
      questions.append(self.get_areas_questions(AreasID.MATHEMATICS))
      return questions

   def get_areas_questions(self, area): #45 questoes  11 facil / 23 normal / 11 dificil
      questions = []
      easy_questions = self.filter_questions(area, "easy")
      questions.append(self.choose_questions(easy_questions))
      normal_questions = self.filter_questions(area, "normal")
      questions.append(self.choose_questions(normal_questions))
      hard_questions = self.filter_questions(area, "hard")
      questions.append(self.choose_questions(hard_questions))
      return questions

   def filter_questions(self, area_id, difficulty): # dissertativas / dificuldade / area
      rating = "BETWEEN 0.8 AND 1.2"
      rating = "< 0.8" if difficulty == "easy" else rating
      rating = "> 1.5" if difficulty == "hard" else rating
      filters = {"area_id": area_id, "rating": rating, "is_essay": "= false", }
      questions = QuestionDAO().get_filtered_questions(filters)
      return questions
   
   def choose_questions(self, questions: List[Question]): #distribuir as questões pelas habilidades
      abilities = [question.get_ability_id() for question in questions]
      chosen_questions = []
      #pegar as abilities
      #dividir a mesma quantidade pra cada e distribuir  
      return chosen_questions


