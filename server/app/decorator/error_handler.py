from app import app
from app.domain.errors.api_exception import ApiException
from flask import jsonify, request

@app.errorhandler(ApiException)
def handle_auth_error(error):
    response = jsonify(sucess=False, errors=error.to_json())
    response.status_code = 400
    print(error.to_json())
    return response

@app.errorhandler(Exception)
def handle_error(error):
    print(error)