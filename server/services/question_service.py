from domain.errors.api_exception import *

class QuestionService:
    def __init__(self, question_repository):
        self.question_repository = question_repository
    
    def get_question(self, user_id):
        
        #Obter notas por habilidades
        
        
        #Selecionar a habilidade a praticar 
        
        
        #Encontrar a questão
        
        result = self.question_repository.get_question("10de8cc6-85f4-4969-ade9-0d9346c70453")
        return result.to_json()
    
    def insert_question_answer(self, user_id, answer, duration):
        #Calcular nova nota do aluno
        
        #Calcular nova nota da questão
        
        #Inserir no banco de dados.
        print(answer)
        print(duration)
        
        pass