class History_of_Mock_exam:
    def __init__(self, id, languages_grade,  humanities_grade, mathematics_grade, natural_science_grade, general_grade, user_id, created_at, questions, is_open, answers, durations, ratings, correct_answers, duration_total):
      self.id = id
      self.languages_grade = languages_grade       
      self.humanities_grade = humanities_grade
      self.mathematics_grade = mathematics_grade
      self.natural_science_grade = natural_science_grade
      self.general_grade = general_grade
      self.user_id = user_id
      self.created_at = created_at
      self.questions = questions
      self.answers = answers
      self.durations = durations
      self.ratings = ratings
      self.correct_answers = correct_answers
      self.is_open = is_open
      self.duration_total = duration_total
        
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
         'answers': self.answers,
         'durations': self.durations,
         'ratings': self.ratings,
         'correct_answers': self.correct_answers,
         'is_open': self.is_open,
         'duration_total': self.duration_total
      }