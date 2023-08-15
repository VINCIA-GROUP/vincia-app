class ChatMessages:
    def __init__(self, id, history_of_question_id, role, content, create_date, sequence):
        self.id = id
        self.history_of_question_id = history_of_question_id
        self.role = role
        self.content = content
        self.create_date = create_date
        self.sequence = sequence

    def to_json(self):
        return {
            "role": self.role,
            "content": self.content
        }