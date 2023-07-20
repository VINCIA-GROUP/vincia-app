from domain.entities.entity import entity


class HistoryOfQuestion(entity):
    def __init__(self, id, create_at, answer_at, hit_level,  time, question_id, user_id, calculate_rating):
        self.id = id
        self.create_at = create_at
        self.answer_at = answer_at
        self.hit_level = hit_level
        self.time = time
        self.question_id = question_id
        self.user_id = user_id
        self.calculate_rating = calculate_rating
    
