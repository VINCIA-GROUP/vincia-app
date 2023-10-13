class History_of_Mock_exam:
    def __init__(self, id, duration, languages_grade,  humanities_grade, mathematics_grade, natural_science_grade, general_grade, user_id, created_at, questions, answers, durations, is_open):
      self.id = id
      self.duration = duration
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
      self.is_open = is_open
        
    def to_json(self):
      return {
         'id': self.id,
         'duration': self.duration,
         'languages_grade': self.languages_grade,
         'humanities_grade': self.humanities_grade,
         'mathematics_grade': self.mathematics_grade,
         'natural_science_grade': self.natural_science_grade,
         'general_grade': self.general_grade,
         'user_id': self.user_id,
         'created_at': self.created_at,
         'questions': self.questions,
         'answers': self.answers,
         'is_open': self.is_open
      }