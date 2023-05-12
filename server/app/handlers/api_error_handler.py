from flask import jsonify
from app import app
from domain.errors.api_errors import ApiError

@app.errorhandler(ApiError)
def handle_auth_error(ex):
    response = jsonify(ex.error_message)
    response.status_code = 400
    return response


