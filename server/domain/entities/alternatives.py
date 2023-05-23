from domain.entities.entity import entity


class Alternatives(entity):
    def __init__(self, id, text):
        self.id = id
        self.text = text
        
