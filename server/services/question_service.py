from domain.errors.api_exception import *
from datetime import datetime
import uuid

class QuestionService:
    def __init__(self, question_repository, history_question_repository):
        self.question_repository = question_repository
        self.history_question_repository = history_question_repository
    
    def get_question(self, user_id):
        
        #Obter notas por habilidades
        
        
        #Selecionar a habilidade a praticar 
        
        
        #Encontrar a questão
        
        result = self.question_repository.get_by_id("10de8cc6-85f4-4969-ade9-0d9346c70453")
        return result.to_json()
    
    def insert_question_answer(self, history_question_id, user_id, question_id, answer, duration):
        #Calcular nova nota do aluno
        
        #Calcular nova nota da questão
        
        #Inserir no banco de dados.
     
        
        self.history_question_repository.create(history_question_id, datetime.now(), 1, 0, duration, question_id, user_id)
        
        print(answer)
        print(duration)
        
  