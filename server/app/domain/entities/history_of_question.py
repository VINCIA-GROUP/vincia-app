class HistoryOfQuestion:
    def __init__(self, id=None, create_at=None, answer_at=None, hit_level=None,  time=None, question_id=None, user_id=None, calculate_rating=None):
        self.id = id
        self.create_at = create_at
        self.answer_at = answer_at
        self.hit_level = hit_level
        self.time = time
        self.question_id = question_id
        self.user_id = user_id
        self.calculate_rating = calculate_rating
    
