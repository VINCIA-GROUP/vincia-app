from flask import jsonify, request, session
from app import app
from app import connection_pool
from app.controllers.base_controller import success_api_response
from app.decorator.requires_auth import requires_auth
from app.repositories.abilities_rating_repository import AbilitiesRatingRepository
from app.repositories.ability_repository import AbilityRepository
from app.services.ability_service import AbilityService



@app.route("/api/ability", methods=["GET"], endpoint="ability")
@requires_auth(None)
def get_question(): 
        connection = connection_pool.get_connection()
        ability_rating_repository = AbilitiesRatingRepository(connection)
        abilities_repository = AbilityRepository(connection)
        service = AbilityService(ability_rating_repository, abilities_repository)
        
        user_id = session.get('current_user').get('sub')
        response = service.get_average_rating(user_id)
        
        connection_pool.release_connection(connection)
        return success_api_response(data=response)