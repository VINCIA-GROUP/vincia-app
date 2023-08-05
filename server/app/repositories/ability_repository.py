from psycopg2 import DatabaseError
from app.domain.entities.ability import Ability

class AbilityRepository():
   def __init__(self, connection):
      self.connection = connection

   def get_all(self):
      abilities = []
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM abilities;")
         rows = self.cursor.fetchall()
         for row in rows:
            ability = Ability(*row)
            abilities.append(ability)
         cursor.close()
      except DatabaseError as error:
         print('AbilityRepository - get_all - ' + error)
      return abilities

   def get_by_id(self, id):
      abilitiy = Ability()
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM abilities a WHERE a.id = %s;", (id,))
         row = self.cursor.fetchone()
         abilitiy = Ability(*row)
         cursor.close()
      except DatabaseError as error:
         print('AbilityRepository - get_by_id - ' + error)
      return abilitiy

   def get_by_name(self, name):
      abilitiy = Ability()
      try:
         cursor = self.connection.cursor()
         cursor.execute("SELECT * FROM abilities a WHERE a.id = %s;", (name,))
         row = self.cursor.fetchone()
         abilitiy = Ability(*row)
         cursor.close()
      except DatabaseError as error:
         print('AbilityRepository - get_by_name - ' + error)
      return abilitiy
   
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