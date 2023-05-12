from domain.entities.entity import entity


class Question(entity):
    def __init__(self, statement, answer, difficulty, is_essay):
        self.statement = statement
        self.answer = answer
        self.difficulty = difficulty
        self.is_wssay = is_essay
    
    
        
        
