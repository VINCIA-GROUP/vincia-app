from app.domain.entities.area import Area
from app.repositories.repository import Repository

class AreaRepository(Repository):
   def __init__(self, connection):
      super().__init__(connection, Area)

   def get_all(self):
      return super().get_many(query="SELECT id, name, description FROM areas;", params="")

   def get_by_id(self, id):
      return super().get_one(
         query="SELECT id, name, description FROM areas  WHERE id = %s;", 
         params=(id,)
      )

   def get_by_name(self, name): 
      return super().get_one(
         query="SELECT id, name, description FROM areas WHERE name = %s;", 
         params=(name,)
      )