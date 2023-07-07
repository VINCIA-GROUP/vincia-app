from flask import jsonify, request, session
from app import app
from services.question_service import QuestionService
from domain.errors.api_exception import ApiException
from app.controllers.base_controller import *
from infra.repositories.questions_repository import QuestionsRepository
from app.decorator.requires_auth import requires_auth
from app import connection


@app.route("/api/question", methods=["GET"], endpoint="question")
@requires_auth(None)
def get_question(): 
        repository = QuestionsRepository(connection)
        service = QuestionService(repository)
        
        user_id = session.get('current_user').get('sub')
        response = service.get_question(user_id)
        return success_api_response(data=response)

    
@app.route("/api/question/answer", methods=["POST"], endpoint="question/answer")
@requires_auth(None)
def post_answer(): 
        repository = QuestionsRepository(connection)
        service = QuestionService(repository)
        
        user_id = session.get('current_user').get('sub')
        data = request.get_json()
        answer = data.get('answer')
        duration = data.get('duration')
        history_question_id = data.get('historyQuestionId')
        
        response = service.insert_question_answer(history_question_id, user_id, answer, duration)
        return success_api_response(data=response)