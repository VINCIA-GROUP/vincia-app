from flask import request, session
from app import app
from app import connection_pool
from app.controllers.base_controller import success_api_response
from app.decorator.requires_auth import requires_auth
from app.repositories.question_repository import QuestionsRepository
from app.repositories.history_of_questions_repository import HistoryOfQuestionsRepository
from app.services.mock_exam_service import MockExamService

@app.route("/api/mock-exam/questions", methods=["GET"], endpoint="mock-exam/questions")
@requires_auth(None)
def questions():
   connection = connection_pool.get_connection()
   questions_repository = QuestionsRepository(connection)
   history_of_questions_repository = HistoryOfQuestionsRepository(connection)
   questions = MockExamService(questions_repository, history_of_questions_repository).get_mock_exam_questions()
   connection_pool.release_connection(connection)
   return success_api_response(data=questions)

@app.route("/api/mock-exam/submmit", methods=["POST"], endpoint="mock-exam/submmit")
@requires_auth(None)
def submmit():
   connection = connection_pool.get_connection()
   questions_repository = QuestionsRepository(connection)
   history_of_questions_repository = HistoryOfQuestionsRepository(connection)
   user_id = session.get('current_user').get('sub')
   data = request.get_json()
   answers = data.get('answers')
   result = MockExamService(questions_repository, history_of_questions_repository).submit_answer(user_id, answers)
   connection_pool.release_connection(connection)
   return success_api_response(data=result)