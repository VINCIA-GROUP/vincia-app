# app/controllers/essay_controller.py
from flask import request, jsonify
from app import app
from app.services.essay_service import EssayService
from app.repositories.essay_repository import EssayRepository
from app.repositories.essay_additional_text_repository import EssayAdditionalTextRepository
from app.repositories.essay_theme_repository import EssayThemeRepository
from app import connection_pool
from app.domain.entities.essay import Essay
from app.decorator.requires_auth import requires_auth
from flask import session


# Instantiate the repositories and service
connection = connection_pool.get_connection()
essay_repository = EssayRepository(connection)
essay_additional_text_repository = EssayAdditionalTextRepository(connection)
essay_theme_repository = EssayThemeRepository(connection)
essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)

@app.route("/api/essay/history", methods=["GET"])
@requires_auth(None)
def get_essay_history():
    user_id = session.get('current_user').get('sub')
    essay_history = essay_service.get_essay_history(user_id)
    return jsonify([essay.to_dict() for essay in essay_history])

@app.route("/api/essay/unfinished/<string:user_id>", methods=["GET"])
def get_unfinished_essays(user_id):
    user_id = session.get('current_user').get('sub')
    unfinished_essays = essay_service.get_unfinished_essays(user_id)
    return jsonify([essay.to_dict() for essay in unfinished_essays])

@app.route("/api/essay", methods=["POST"])
def save_essay():
    user_id = session.get('current_user').get('sub')
    data = request.get_json()
    essay = Essay(**data)
    essay_service.save_essay(essay)
    return jsonify(success=True), 201

@app.route("/api/essay/<string:essay_id>", methods=["DELETE"])
def delete_essay(essay_id):
    user_id = session.get('current_user').get('sub')
    essay_service.delete_essay(essay_id)
    return jsonify(success=True)

@app.route("/api/essay/analysis", methods=["POST"])
def get_essay_analysis():
    data = request.get_json()
    essay_id = data.get("essay_id")
    user_id = data.get("user_id")
    theme_id = data.get("theme_id")
    theme_title = data.get("theme_title")
    essay_title = data.get("essay_title")
    essay_content = data.get("essay_content")
    
    analysis = essay_service.get_essay_analysis(essay_id, user_id, theme_id, theme_title, essay_title, essay_content)
    return jsonify(analysis)
