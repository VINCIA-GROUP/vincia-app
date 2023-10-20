import base64
from flask import Flask, request, jsonify
from app import app
from app.repositories.essay_additional_text_repository import EssayAdditionalTextRepository
from app.repositories.essay_repository import EssayRepository
from app.repositories.essay_theme_repository import EssayThemeRepository
from app.services.essay_service import EssayService
from app.decorator.requires_auth import requires_auth
from app import connection_pool


@app.route("/api/essay/transcribe", methods=['POST'])
@requires_auth(None)
def transcribe_essay():
    connection = connection_pool.get_connection()
    essay_repository = EssayRepository(connection)
    essay_additional_text_repository = EssayAdditionalTextRepository(connection)
    essay_theme_repository = EssayThemeRepository(connection)
    essay_service = EssayService(essay_repository, essay_additional_text_repository, essay_theme_repository)


    data = request.get_json()  # Get the JSON payload from the request
    if not data or 'image' not in data:
        print("no image data")
        connection_pool.release_connection(connection)
        return jsonify(error="No image data"), 400

    base64_string = data['image']  # Get the base64 string from the JSON
    try:
        image_data = base64.b64decode(base64_string)  # Decode the base64 string to binary data
    except ValueError:
        connection_pool.release_connection(connection)
        return jsonify(error="Invalid base64 string"), 400

    transcription = essay_service.perform_ocr(image_data)  # Pass the binary data to your OCR method
    if transcription:
        connection_pool.release_connection(connection)
        return jsonify(transcription=transcription)
    connection_pool.release_connection(connection)
    return jsonify(error="Could not transcribe image"), 400
