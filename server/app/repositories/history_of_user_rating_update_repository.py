from app.repositories.repository import Repository

class HistoryOfUserRatingUpdateRepository(Repository):
    def __init__(self, connection): 
        super().__init__(connection, "")   
    
    def create(self, entity):
        return super().update(
            query="INSERT INTO history_of_user_rating_updates (id, create_at, rating, rating_deviation, volatility,  user_id, ability_id) VALUES (%s, %s, %s, %s, %s, %s, %s);",
            params=(entity.id, entity.create_at, entity.rating, entity.rating_deviation, entity.volatility, entity.user_id, entity.ability_id)
        )