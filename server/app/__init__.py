import os
import openai
import psycopg2

from dotenv import load_dotenv
from flask import Flask
from flask import jsonify, request
from app.domain.errors.api_exception import ApiException
from app.controllers.base_controller import *
from utils.db_pool_connection import DatabaseConnection

load_dotenv()

openai.api_key= os.getenv("OPENAI_KEY")

app = Flask(__name__)
app.secret_key = os.environ["APP_SECRET_KEY"]

connection_pool = DatabaseConnection(1, 5)

from app.decorator import error_handler
from app.controllers import test_controller
from app.controllers import question_controller
from app.controllers import chat_controller
from app.decorator import after_request_callback





