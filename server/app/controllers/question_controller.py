from flask import jsonify, request, session
from app import app
from services.question_service import QuestionService
from domain.errors.api_exception import ApiException
from app.controllers.base_controller import *
from infra.repositories.questions_repository import QuestionsRepository
from app.decorator.requires_auth import requires_auth

from app.dao.question_dao import QuestionDAO

@app.route("/api/question/<string:id>", methods=["GET"])
def get_question_teste(id):
        question = QuestionDAO().get_question_by_id(id)
        return success_api_response(data=question.to_json())

@app.route("/api/question", methods=["GET"], endpoint="question")
@requires_auth(None)
def get_question(): 
        repository = QuestionsRepository()
        service = QuestionService(repository)
        
        user_id = session.get('current_user').get('sub')
        response = service.get_question(user_id)
        return success_api_response(data=response)

    
@app.route("/api/question/answer", methods=["POST"], endpoint="question/answer")
@requires_auth(None)
def post_answer(): 
        repository = QuestionsRepository()
        service = QuestionService(repository)
        
        user_id = session.get('current_user').get('sub')
        data = request.get_json()
        answer = data.get('answer')
        duration = data.get('duration')
        
        response = service.insert_question_answer(user_id, answer, duration)
        return success_api_response(data=response)