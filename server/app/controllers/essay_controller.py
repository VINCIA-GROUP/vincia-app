# app/controllers/essay_controller.py
from flask import request, jsonify, session
from app import app
from app.services.essay_service import EssayService
from app.repositories.essay_repository import EssayRepository
from app.repositories.essay_additional_text_repository import EssayAdditionalTextRepository
from app.repositories.essay_theme_repository import EssayThemeRepository
from app import connection_pool
from app.domain.entities.essay import Essay
from app.decorator.requires_auth import requires_auth


@app.route("/api/essay/history", methods=["GET"], endpoint="essay/history")
@requires_auth(None)
def get_essay_history():
    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)

    user_id = session.get('current_user').get('sub')
    essay_history = essay_service.get_essay_history(user_id)

    connection_pool.release_connection(connection)
    return jsonify([essay.to_json() for essay in essay_history])

@app.route("/api/essay/unfinished", methods=["GET"], endpoint="essay/unfinished")
@requires_auth(None)
def get_unfinished_essays():

    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)

    user_id = session.get('current_user').get('sub')
    unfinished_essays = essay_service.get_unfinished_essays(user_id)

    connection_pool.release_connection(connection)
    return jsonify([essay.to_json() for essay in unfinished_essays])


@app.route("/api/essay", methods=["POST"])
def save_essay():

    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)


    user_id = session.get('current_user').get('sub')
    data = request.get_json()
    essay = Essay(**data)
    essay_service.save_essay(essay)

    connection_pool.release_connection(connection)
    return jsonify(success=True), 201

@app.route("/api/essay/create", methods=["POST"], endpoint="essay/create")
@requires_auth(None)
def create_new_essay():
    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)

    user_id = session.get('current_user').get('sub')
    data = request.get_json()
    
    if 'theme_id' not in data:
        connection_pool.release_connection(connection)
        return jsonify(error="theme_id is required"), 400  # Return a 400 Bad Request if theme_id is missing

    theme_id = data['theme_id']
    title = data['title']
    essay_service.create_new_essay(theme_id, user_id, title)

    essay = essay_service.get_newest_created_essay(user_id)

    connection_pool.release_connection(connection)
    return jsonify(essay.to_json()), 201
    # return jsonify(success=True), 201

@app.route("/api/essay/<string:essay_id>", methods=["DELETE"])
def delete_essay(essay_id):

    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)


    user_id = session.get('current_user').get('sub')
    essay_service.delete_essay(essay_id)

    connection_pool.release_connection(connection)
    return jsonify(success=True)

@app.route("/api/essay/analysis", methods=["POST"], endpoint="essay/analysis")
@requires_auth(None)
def get_essay_analysis():

    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)

    data = request.get_json()
    id = data.get("id")
    user_id = session.get('current_user').get('sub')
    theme_id = data.get("theme_id")
    essay_title = data.get("essay_title")
    essay_content = data.get("essay_content")

    analysis = essay_service.get_essay_analysis(id, user_id, theme_id, essay_title, essay_content)
    
    connection_pool.release_connection(connection)
    return jsonify(analysis)
