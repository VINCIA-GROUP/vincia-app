from domain.entities.entity import entity


class Ability(entity):
    def __init__(self, id, name, description, area_id):
        self.id = id
        self.name = name
        self.decription = description
        self.area_id = area_id
        
