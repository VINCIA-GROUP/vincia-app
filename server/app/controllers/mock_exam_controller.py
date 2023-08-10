from flask import jsonify, request, session
from app import app
from app import connection_pool
from app.controllers.base_controller import success_api_response
from app.decorator.requires_auth import requires_auth
from app.repositories.question_repository import QuestionsRepository
from app.services.mock_exam_service import MockExamService

@app.route("/api/mock-exam/get-questions", endpoint="mock-exam/get-questions")
def get_questions():
   connection = connection_pool.get_connection()
   questions_repository = QuestionsRepository(connection)
   questions = MockExamService(questions_repository).get_mock_exam_questions()
   for i, question in enumerate(questions):
      questions[i] = question.to_json()
   connection_pool.release_connection(connection)
   return success_api_response(data=questions)
