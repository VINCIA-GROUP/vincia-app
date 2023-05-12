
from flask import jsonify, request
from app import app
from services.question_service import QuestionService
from domain.errors.api_errors import DeuMerda

@app.route("/api/question", methods=["GET"])
def get_question():
    ##user_id = current_token.sub
    
    raise DeuMerda()
    
    service = QuestionService()
    response = service.get_question()
    return jsonify(message=response)
