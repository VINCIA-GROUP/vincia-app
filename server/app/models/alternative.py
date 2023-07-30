class Alternative():
   def __init__(self, id, text, question_id):
      self._id = id
      self._text = text
      self._question_id = question_id

   def get_id(self):
      return self._id
   
   def get_text(self):
      return self._text
   
   def get_quetion_id(self):
      return self._question_id
   
   def to_json(self):
      return {
         "id": self._id,
         "text": self._text,
         "question_id": self._question_id
      }