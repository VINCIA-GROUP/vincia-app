class Alternative:
   def __init__(self, id, text):
      self.id = id
      self.text = text
   
   def to_json(self):
      return {
         "id": self.id,
         "text": self.text,
      }