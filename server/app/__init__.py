import os
import openai
import psycopg2

from dotenv import load_dotenv
from flask import Flask
from flask import jsonify, request
from domain.errors.api_exception import ApiException
from app.controllers.base_controller import *

load_dotenv()

openai.api_key= os.getenv("OPENAI_KEY")

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

sc = os.environ["CONNECTION_STRING_DB"]    
connection = psycopg2.connect(sc, sslmode='require',)

@app.errorhandler(ApiException)
def handle_auth_error(error):
    response = jsonify(sucess=False, errors=error.to_json())
    response.status_code = 400
    return response

from app.controllers import test_controller
from app.controllers import question_controller
from app.controllers import chat_controller





