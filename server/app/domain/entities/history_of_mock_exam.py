class History_of_Mock_exam:
    def __init__(self, id, languages_grade,  humanities_grade, mathematics_grade, natural_science_grade, general_grade, user_id, created_at, questions, is_open, answers, durations, ratings, duration_total, correct_answers):
      self.id = id
      self.languages_grade = languages_grade       
      self.humanities_grade = humanities_grade
      self.mathematics_grade = mathematics_grade
      self.natural_science_grade = natural_science_grade
      self.general_grade = general_grade
      self.user_id = user_id
      self.created_at = created_at
      self.questions = questions
      self.is_open = is_open
      self.answers = answers
      self.durations = durations
      self.ratings = ratings
      self.duration_total = duration_total
      self.correct_answers = correct_answers
        
    def to_json(self):
      return {
         'id': self.id,
         'languages_grade': self.languages_grade,
         'humanities_grade': self.humanities_grade,
         'mathematics_grade': self.mathematics_grade,
         'natural_science_grade': self.natural_science_grade,
         'general_grade': self.general_grade,
         'user_id': self.user_id,
         'created_at': self.created_at,
         'questions': self.questions,
         'is_open': self.is_open,
         'answers': self.answers,
         'durations': self.durations,
         'ratings': self.ratings,
         'duration_total': self.duration_total,
         'correct_answers': self.correct_answers
      }