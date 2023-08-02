from app.models.area import Area
from utils.db_manager import DatabaseManager

class AreaDAO():

   def get_all_areas():
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM areas;")
         rows = db.cursor.fetchall()
         areas = []
         for row in rows:
            area = Area(*row)
            areas.append(area)
         return areas

   def get_area_by_id(id):
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM areas a WHERE a.id = %s;", (id,))
         row = db.cursor.fetchall()[0]
         area = Area(*row)
         return area

   def get_area_by_name(name): 
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM areas a WHERE a.name = %s;", (name,))
         row = db.cursor.fetchall()[0]
         area = Area(*row)
         return area