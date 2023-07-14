from domain.entities.ability import Ability
from infra.repositories.repository import Repository


class AbilitiesRepository(Repository):
    def __init__(self, connect): 
        super().__init__(connect)   
        
    def get_abilities_list(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, description, area_id FROM abilities;")
        if(cursor.rowcount <= 0):
            cursor.close()
            return None
        abilities_tuple = cursor.fetchall()
        list = []
        for ability_tuple in abilities_tuple:
            id, name, description, area_id = ability_tuple
            list.append(Ability(id, name, description, area_id))
        cursor.close()
        return list
    