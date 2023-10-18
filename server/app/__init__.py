import os
from flask_cors import CORS
import openai

from dotenv import load_dotenv
from flask import Flask
from flask import jsonify, request
from app.domain.errors.api_exception import ApiException
from app.controllers.base_controller import *
from utils.db_pool_connection import DatabaseConnection

load_dotenv()

openai.api_key= os.getenv("OPENAI_KEY")

app = Flask(__name__)
CORS(app)
app.secret_key = os.getenv("APP_SECRET_KEY")

connection_pool = DatabaseConnection(1, 5)

from app.decorator import error_handler
from app.controllers import test_controller
from app.controllers import question_controller
from app.controllers import mock_exam_controller
from app.controllers import chat_controller
from app.controllers import ability_controller
from app.controllers import essay_transcibe_controller
from app.controllers import essay_theme_controller
from app.controllers import essay_additional_text_controller
