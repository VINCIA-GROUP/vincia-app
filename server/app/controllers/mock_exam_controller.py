from flask import request, session
from app import app
from app import connection_pool
from app.controllers.base_controller import success_api_response
from app.decorator.requires_auth import requires_auth
from app.repositories.question_repository import QuestionsRepository
from app.repositories.history_of_questions_repository import HistoryOfQuestionsRepository
from app.services.mock_exam_service import MockExamService

@app.route("/api/mock-exam/get-questions", methods=["GET"], endpoint="mock-exam/get-questions")
@requires_auth(None)
def get_questions():
   connection = connection_pool.get_connection()
   questions_repository = QuestionsRepository(connection)
   questions = MockExamService(questions_repository).get_mock_exam_questions()
   connection_pool.release_connection(connection)
   return success_api_response(data=questions)

@app.route("/api/mock-exam/question-answer", methods=["POST"], endpoint="mock-exam/question-answer")
@requires_auth(None)
def post_answer():
   connection = connection_pool.get_connection()
   history_of_questions = HistoryOfQuestionsRepository(connection)
   
   

   return success_api_response()

@app.route("/api/mock-exam/submmit", methods=["POST"], endpoint="mock-exam/submmit")
@requires_auth(None)
def submmit_exam():
   connection = connection_pool.get_connection()
   
   return success_api_response()