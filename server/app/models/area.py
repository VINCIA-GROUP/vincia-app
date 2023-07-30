class Area():
   def __init__(self, id, name, description):
      self._id = id
      self._name = name
      self._description = description

   def get_id(self):
      return self._id
   
   def get_name(self):
      return self._name
   
   def get_description(self):
      return self._description
   
   def to_json(self):
      return {
         'id': self._id,
         'name': self._name,
         'description': self._description
      }