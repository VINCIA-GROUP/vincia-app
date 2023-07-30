class Ability():
   def __init__(self, id, name, description, area_id):
      self._id = id
      self._name = name
      self._description = description
      self._area_id = area_id
    
   def get_id(self):
      return self._id
    
   def get_name(self):
      return self._name
    
   def get_description(self):
      return self._description
    
   def get_area_id(self):
      return self._area_id
    
   def to_json(self):
      return {
         'id': self._id,
         'name': self._name,
         'description': self._description,
         'area_id': self._area_id
      }