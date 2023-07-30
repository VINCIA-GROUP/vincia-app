from app.models.alternative import Alternative
from typing import List

class Question():
    def __init__(self, id, statement, answer, rating, rating_deviation, volatility, last_rating_update, is_essay, ability_id):
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
    
    def get_id(self):
        return self._id
    
    def get_statement(self):
        return self._statement
    
    def get_alternatives(self):
        return self._alternatives
    
    def set_alternatives(self, alternatives):
        self._alternatives = alternatives

    def get_answer(self):
        return self._answer
    
    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        self._rating = rating

    def get_rating_deviation(self):
        return self._rating_deviation
    
    def set_rating_deviation(self, rating_deviation):
        self._rating_deviation = rating_deviation

    def get_volatility(self):
        return self._volatility
    
    def set_volatility(self, volatility):
        self._volatility = volatility

    def get_last_rating_update(self):
        return self._last_rating_update
    
    def set_last_rating_update(self, last_rating_update):
        self._last_rating_update = last_rating_update
        
    def get_is_essay(self):
        return self._is_essay
    
    def get_ability_id(self):
        return self._ability_id
    
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