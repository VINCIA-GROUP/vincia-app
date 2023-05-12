from domain.entities.entity import entity


class Ability(entity):
    def __init__(self, name, description):
        self.name = name
        self.decription = description
        
