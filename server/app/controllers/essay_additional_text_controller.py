# app/controllers/essay_additional_text_controller.py

from flask import request, jsonify
from app import app
from app.services.essay_additional_text_service import EssayAdditionalTextService
from app.repositories.essay_additional_text_repository import EssayAdditionalTextRepository
from app import connection_pool

connection = connection_pool.get_connection()
essay_additional_text_repository = EssayAdditionalTextRepository(connection)
essay_additional_text_service = EssayAdditionalTextService(essay_additional_text_repository)

@app.route("/api/essay/additional-text/<string:text_id>", methods=["GET"])
def get_additional_text_by_id(text_id):
    additional_text = essay_additional_text_service.get_additional_text_by_id(text_id)
    if additional_text:
        return jsonify(additional_text.to_dict())
    return jsonify(error="Additional Text not found"), 404

@app.route("/api/essay/additional-texts/<string:theme_id>", methods=["GET"])
def get_additional_texts_by_theme_id(theme_id):
    additional_texts = essay_additional_text_service.get_additional_texts_by_theme_id(theme_id)
    return jsonify([text.to_dict() for text in additional_texts])

@app.route("/api/essay/additional-text", methods=["POST"])
def create_additional_text():
    data = request.get_json()
    additional_text_id = data.get("text_id")
    theme_id = data.get("theme_id")
    title = data.get("title")
    content = data.get("content")
    essay_additional_text_service.create_additional_text(additional_text_id, theme_id, title, content)
    return jsonify(success=True), 201

@app.route("/api/essay/additional-text/<string:text_id>", methods=["PUT"])
def modify_additional_text(text_id):
    data = request.get_json()
    theme_id = data.get("theme_id")
    title = data.get("title")
    content = data.get("content")
    essay_additional_text_service.modify_additional_text(theme_id, title, content, text_id)
    return jsonify(success=True)

@app.route("/api/essay/additional-text/<string:text_id>", methods=["DELETE"])
def remove_additional_text(text_id):
    essay_additional_text_service.remove_additional_text(text_id)
    return jsonify(success=True)
