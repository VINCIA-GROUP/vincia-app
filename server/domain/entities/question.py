from domain.entities.entity import entity
from datetime import datetime

class Question(entity):
    def __init__(self, id, statement, answer, is_essay, rating=0, rating_deviation=0, volatility=0, last_rating_update=datetime.min):
        self.id = id
        self.statement = statement
        self.answer = answer
        self.rating= rating
        self.rating_deviation = rating_deviation
        self.volatility = volatility
        self.last_rating_update = last_rating_update
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
            "rating":self.rating,
            "is_essay":self.is_essay,
            "alternatives": allist
        }
    
        
        
