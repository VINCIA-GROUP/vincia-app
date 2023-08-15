from app.domain.entities.alternatives import Alternative
from typing import List
from datetime import datetime

class Question:
    def __init__(self, id, statement, answer,  is_essay, ability_id, rating=0, rating_deviation=0, volatility=0, last_rating_update=datetime.min):
      self.id = id
      self.statement = statement
      self.alternatives: List[Alternative] = []
      self.answer = answer       
      self.rating = rating
      self.rating_deviation = rating_deviation
      self.volatility = volatility
      self.last_rating_update = last_rating_update
      self.is_essay = is_essay
      self.ability_id = ability_id
        
    def to_json(self):
        for i, alternative in enumerate(self.alternatives):
            self.alternatives[i] = alternative.to_json()
        return {
            'id': self.id,
            'statement': self.statement,
            'answer': self.answer,
            'rating': self.rating,
            'is_essay': self.is_essay,
            'alternatives': self.alternatives,
        }