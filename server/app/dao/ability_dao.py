from app.models.ability import Ability
from utils.db_manager import DatabaseManager

class AbilityDAO():

   def get_all_abilities():
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM abilities;")
         rows = db.cursor.fetchall()
         abilities = []
         for row in rows:
            ability = Ability(*row)
            abilities.append(ability)
         return abilities

   def get_ability_by_id(self, id):
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM abilities a WHERE a.id = %s;", (id,))
         row = db.cursor.fetchall()[0]
         abilitiy = Ability(*row)
         return abilitiy

   def get_ability_by_name(self, name):
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM abilities a WHERE a.id = %s;", (name,))
         row = db.cursor.fetchall()[0]
         abilitiy = Ability(*row)
         return abilitiy