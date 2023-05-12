from domain.entities.entity import entity


class Area(entity):
    def __init__(self, name, description):
        self.name = name
        self.decription = description
        
