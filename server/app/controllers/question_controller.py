
from flask import jsonify, request
from app import app
from services.question_service import QuestionService
from domain.errors.api_exception import ApiException
from app.controllers.base_controller import *

@app.route("/api/question", methods=["GET"])
def get_question(): 
        service = QuestionService()
        response = service.get_question()
        return success_api_response(data=response)

    
