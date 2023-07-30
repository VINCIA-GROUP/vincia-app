from flask import jsonify, request, session
from app import app
from app.decorator.requires_auth import requires_auth
from app.services.mock_exam_service import MockExamService
from app.models.question import Question
from base_controller import success_api_response
from typing import List

@app.route("/api/mock-exam/get-questions", methods=["GET"])
def get_questions():
   questions: List[Question] = MockExamService.get_mock_exam_questions()
   for i, question in enumerate(questions):
      questions[i] = question.to_json()
   return success_api_response(data=questions)
