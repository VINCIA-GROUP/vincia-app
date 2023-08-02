class Ability:
    def __init__(self, id, name, description, area_id):
        self.id = id
        self.name = name
        self.description = description
        self.area_id = area_id

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'area_id': self.area_id
        }
