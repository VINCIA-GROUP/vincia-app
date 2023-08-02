class HistoryOfUserRatingUpdate:
    def __init__(self, id, create_at, rating, rating_deviation, volatility, user_id, ability_id):
        self.id = id
        self.create_at = create_at
        self.rating = rating
        self.rating_deviation = rating_deviation
        self.volatility = volatility
        self.user_id = user_id
        self.ability_id = ability_id