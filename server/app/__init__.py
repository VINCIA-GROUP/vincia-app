import os

from dotenv import load_dotenv
from flask import Flask
from flask import jsonify, request
from domain.errors.api_exception import ApiException
from app.controllers.base_controller import *

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]


@app.errorhandler(ApiException)
def handle_auth_error(error):
    response = jsonify(sucess=False, data=error.to_json())
    response.status_code = 400
    return response

from app.controllers import test_controller
from app.controllers import question_controller





