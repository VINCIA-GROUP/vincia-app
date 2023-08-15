class HistoryOfQuestionRatingUpdate:
    def __init__(self, id, create_at, rating, rating_deviation, volatility, question_id):
        self.id = id
        self.create_at = create_at
        self.rating = rating
        self.rating_deviation = rating_deviation
        self.volatility = volatility
        self.question_id = question_id