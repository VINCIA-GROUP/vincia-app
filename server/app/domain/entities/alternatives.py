class Alternative:
   def __init__(self, id, text, question_id):
      self.id = id
      self.text = text
      self.question_id = question_id
   
   def to_json(self):
      return {
         "id": self.id,
         "text": self.text,
         "question_id": self.question_id
      }