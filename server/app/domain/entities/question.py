from app.domain.entities.alternatives import Alternative
from typing import List
from datetime import datetime

class Question:
    def __init__(self, id, statement, answer,  is_essay, ability_id, rating=0, rating_deviation=0, volatility=0, last_rating_update=datetime.min):
      self._id = id
      self._statement = statement
      self._alternatives: List[Alternative] = []
      self._answer = answer       
      self._rating = rating
      self._rating_deviation = rating_deviation
      self._volatility = volatility
      self._last_rating_update = last_rating_update
      self._is_essay = is_essay
      self._ability_id = ability_id
        
    def to_json(self):
        for i, alternative in enumerate(self._alternatives):
            self._alternatives[i] = alternative.to_json()
        return {
            'id': self._id,
            'statement': self._statement,
            'alternatives': self._alternatives,
            'answer': self._answer,
            'rating': self._rating,
            'rating_deviation': self._rating_deviation,
            'volatility': self._volatility,
            'last_rating_update': self._last_rating_update,
            'is_essay': self._is_essay,
            'ability_id': self._ability_id
        }