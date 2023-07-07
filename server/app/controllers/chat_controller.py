from flask import jsonify, request, session
from app import app
from infra.repositories.chat_repository import ChatRepository
from infra.repositories.questions_repository import QuestionsRepository
from infra.repositories.history_question_repository import HistoryQuestionsRepository
from services.chat_service import ChatService
from domain.errors.api_exception import ApiException
from app.controllers.base_controller import *
from app.decorator.requires_auth import requires_auth
from app import connection


@app.route("/api/chat", methods=["POST"], endpoint="chat")
def send_message(): 
    
        question_repository = QuestionsRepository(connection)
        history_question_repository = HistoryQuestionsRepository(connection)
        chat_repository = ChatRepository(connection)
        service = ChatService(history_question_repository, question_repository, chat_repository)

        data = request.get_json()
        messages = data.get('messages')
        response = service.send_message("teste", "teste", messages)
        return success_api_response(data=response)