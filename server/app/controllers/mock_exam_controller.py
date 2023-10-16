from flask import request, session
from app import app
from app import connection_pool
from app.controllers.base_controller import success_api_response
from app.decorator.requires_auth import requires_auth
from app.repositories.question_repository import QuestionsRepository
from app.repositories.history_of_questions_repository import HistoryOfQuestionsRepository
from app.repositories.history_of_mock_exam_repository import HistoryOfMockExamRepository
from app.services.mock_exam_service import MockExamService

@app.route("/api/mock-exam/questions", methods=["GET"], endpoint="mock-exam/questions")
@requires_auth(None)
def questions():
   connection = connection_pool.get_connection()
   user_id = session.get('current_user').get('sub')
   result = MockExamService(QuestionsRepository(connection), 
                               HistoryOfQuestionsRepository(connection),
                               HistoryOfMockExamRepository(connection)).get_mock_exam_questions(user_id)
   connection_pool.release_connection(connection)
   return success_api_response(data=result)

@app.route("/api/mock-exam/question/<string:id>", methods=["GET"], endpoint="mock-exam/question")
@requires_auth(None)
def question(id):
   connection = connection_pool.get_connection()
   question = MockExamService(QuestionsRepository(connection), 
                               HistoryOfQuestionsRepository(connection),
                               HistoryOfMockExamRepository(connection)).get_question(id)
   connection_pool.release_connection(connection)
   return success_api_response(data=question)

@app.route("/api/mock-exam/answer", methods=["POST"], endpoint="mock-exam/answer")
@requires_auth(None)
def submmit():
   connection = connection_pool.get_connection()
   user_id = session.get('current_user').get('sub')
   data = request.get_json()
   answers = data.get('answers')
   result = MockExamService(QuestionsRepository(connection),
                            HistoryOfQuestionsRepository(connection),
                            HistoryOfMockExamRepository(connection)).submit_answer(user_id, answers)
   connection_pool.release_connection(connection)
   return success_api_response(data=result)

@app.route("/api/mock-exam/submmit", methods=["GET"], endpoint="mock-exam/submmit")
@requires_auth(None)
def submmit():
   connection = connection_pool.get_connection()
   grade = MockExamService(QuestionsRepository(connection),
                           HistoryOfQuestionsRepository(connection),
                           HistoryOfMockExamRepository(connection)).submmit()
   connection_pool.release_connection(connection)
   return success_api_response(data=grade)