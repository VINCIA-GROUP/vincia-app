from domain.entities.entity import entity


class ChatMessages(entity):
    def __init__(self, id, history_of_question_id, role, content, create_date):
        self.id = id
        self.history_of_question_id = history_of_question_id
        self.role = role
        self.content = content
        self.create_date = create_date
        
    def to_json(self):
        return {
            "role": self.role,
            "content": self.content
        }