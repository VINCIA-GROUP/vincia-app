from domain.errors.api_exception import *

class QuestionService:
    
    def get_question(self):
        raise ApiException(ApiError("11", "Teste etes"))
        return "Question Service"