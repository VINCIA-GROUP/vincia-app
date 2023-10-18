# app/controllers/essay_theme_controller.py
from flask import jsonify, request
from app import app
from app.repositories.essay_theme_repository import EssayThemeRepository
from app.services.essay_theme_service import EssayThemeService
from app import connection_pool

@app.route("/api/essay/theme", methods=["GET"])
def get_all_themes():
    connection = connection_pool.get_connection()
    try:
        essay_theme_repository = EssayThemeRepository(connection)
        service = EssayThemeService(essay_theme_repository)
        themes = service.get_all_themes()
        response_data = [theme.to_json() for theme in themes]
        return jsonify(data=response_data), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        connection_pool.release_connection(connection)

@app.route("/api/essay/theme/<string:theme_id>", methods=["GET"])
def get_theme_by_id(theme_id):
    connection = connection_pool.get_connection()
    try:
        essay_theme_repository = EssayThemeRepository(connection)
        service = EssayThemeService(essay_theme_repository)
        theme = service.get_theme_by_id(theme_id)
        return jsonify(data=theme.to_json()), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        connection_pool.release_connection(connection)

@app.route("/api/essay/theme", methods=["POST"])
def create_theme():
    connection = connection_pool.get_connection()
    essay_theme_repository = EssayThemeRepository(connection)
    service = EssayThemeService(essay_theme_repository)
    
    data = request.get_json()
    theme_id = data.get('theme_id')
    title = data.get('title')
    tag = data.get('tag')
    
    try:
        service.create_theme(theme_id, title, tag)
        return jsonify(status='Theme created successfully.'), 201
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        connection_pool.release_connection(connection)


@app.route("/api/essay/theme/<string:theme_id>", methods=["PUT"])
def update_theme(theme_id):
    connection = connection_pool.get_connection()
    essay_theme_repository = EssayThemeRepository(connection)
    service = EssayThemeService(essay_theme_repository)
    
    data = request.get_json()
    title = data.get('title')
    tag = data.get('tag')
    
    try:
        service.modify_theme(title, tag, theme_id)
        return jsonify(status='Theme updated successfully.'), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        connection_pool.release_connection(connection)


@app.route("/api/essay/theme/<string:theme_id>", methods=["DELETE"])
def delete_theme(theme_id):
    connection = connection_pool.get_connection()
    essay_theme_repository = EssayThemeRepository(connection)
    service = EssayThemeService(essay_theme_repository)
    
    try:
        service.remove_theme(theme_id)
        return jsonify(status='Theme deleted successfully.'), 200
    except Exception as e:
        return jsonify(error=str(e)), 500
    finally:
        connection_pool.release_connection(connection)
