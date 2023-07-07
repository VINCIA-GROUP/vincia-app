from domain.entities.entity import entity


class Question(entity):
    def __init__(self, id, statement, answer, difficulty, is_essay):
        self.id = id
        self.statement = statement
        self.answer = answer
        self.difficulty = difficulty
        self.is_essay = is_essay
        self.alternatives = []
    
    def add_list_alternative(self, alternatives):
        self.alternatives = alternatives
    
    def to_json(self):
        allist = list(map(lambda x: {"id": x.id, "text": x.text}, self.alternatives))
        return {
            "id": self.id,
            "statement":self.statement,
            "answer":self.answer,
            "difficulty":self.difficulty,
            "is_essay":self.is_essay,
            "alternatives": allist
        }
    
        
        
