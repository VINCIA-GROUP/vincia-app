from flask import jsonify, request, session
from app import app
from app.repositories.chat_repository import ChatRepository
from app.repositories.question_repository import QuestionsRepository
from app.repositories.history_of_questions_repository import HistoryOfQuestionsRepository
from app.services.chat_service import ChatService
from app.domain.errors.api_exception import ApiException
from app.controllers.base_controller import *
from app.decorator.requires_auth import requires_auth
from app import connection_pool


@app.route("/api/chat", methods=["POST"], endpoint="chat")
@requires_auth(None)
def send_message(): 
        connection = connection_pool.get_connection()
        question_repository = QuestionsRepository(connection)
        history_question_repository =  HistoryOfQuestionsRepository(connection)
        chat_repository = ChatRepository(connection)
        service = ChatService(history_question_repository, question_repository, chat_repository)

        data = request.get_json()
        user_id = session.get('current_user').get('sub')
        question_id = data.get('questionId')
        message = data.get('message') 
        response = service.send_message(user_id, question_id, message)
        connection_pool.release_connection(connection)
        return success_api_response(data=response)