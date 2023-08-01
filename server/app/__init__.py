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
# Este talvez não seja o melhor geito de criar a conecção.
connection = psycopg2.connect(sc, sslmode='require',)


from app.decorator import error_handler
from app.controllers import test_controller
from app.controllers import question_controller
from app.controllers import chat_controller
from app.decorator import after_request_callback





