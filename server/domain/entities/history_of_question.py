from domain.entities.entity import entity


class HistoryOfQuestion(entity):
    def __init__(self, id, date, hit_level, var_grade, time, question_id, user_id):
        self.id = id
        self.date = date
        self.hit_level = hit_level
        self.var_grade = var_grade
        self.time = time
        self.question_id = question_id
        self.user_id = user_id
    
