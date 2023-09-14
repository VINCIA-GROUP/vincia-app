class HistoryOfQuestion:
    def __init__(self, id=None, create_at=None, hit_level=None,  time=None, question_id=None, history_of_user_rating_update_id=None,user_id=None):
        self.id = id
        self.create_at = create_at
        self.hit_level = hit_level
        self.time = time
        self.question_id = question_id
        self.history_of_user_rating_update_id = history_of_user_rating_update_id
        self.user_id = user_id
    
