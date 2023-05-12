import os

from dotenv import load_dotenv
from flask import Flask
from flask import jsonify, request

load_dotenv()


app = Flask(__name__)
app.secret_key = "secrete"

# Error handler
class AuthError(Exception):
    def __init__(self, error, status_code):
        self.error = error
        self.status_code = status_code

@app.errorhandler(AuthError)
def handle_auth_error(ex):
    response = jsonify(ex.error)
    response.status_code = ex.status_code
    return response

from app.controllers import test_controller
from app.controllers import question_controller



