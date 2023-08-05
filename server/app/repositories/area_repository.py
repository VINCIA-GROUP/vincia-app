from psycopg2 import DatabaseError
from app.domain.entities.area import Area

class AreaRepository():
   def __init__(self, connection):
      self.connection = connection

   def get_all(self):
      areas = []
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM areas;")
         rows = self.cursor.fetchall()
         for row in rows:
            area = Area(*row)
            areas.append(area)
         cursor.close()
      except DatabaseError as error:
         print('AreaRepository - get_all - ' + error)
      return areas

   def get_by_id(self, id):
      area = Area()
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM areas a WHERE a.id = %s;", (id,))
         row = self.cursor.fetchall()[0]
         area = Area(*row)
         cursor.close()
      except DatabaseError as error:
         print('AreaRepository - get_by_id - ' + error)
      return area

   def get_by_name(self, name): 
      area = Area()
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM areas a WHERE a.name = %s;", (name,))
         row = self.cursor.fetchone()
         area = Area(*row)
         cursor.close()
      except DatabaseError as error:
         print('AreaRepository - get_by_name - ' + error)
      return area
   
   def commit(self):
      try:
         self.connection.commit()
         return True
      except DatabaseError as error:
         print('QuestionsRepository - commit - ' + error)
         return False

   def rollback(self):
      try:
         self.connection.rollback()
         return True
      except DatabaseError as error:
         print('QuestionsRepository - rollback - ' + error)
         return False
