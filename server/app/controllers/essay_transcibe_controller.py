import base64
from flask import Flask, request, jsonify
from app import app
from app.services.essay_service import EssayService
from app.decorator.requires_auth import requires_auth

@app.route("/api/essay/transcribe", methods=['POST'])
@requires_auth(None)
def transcribe_essay():
    data = request.get_json()  # Get the JSON payload from the request
    if not data or 'image' not in data:
        print("no image data")
        return jsonify(error="No image data"), 400

    base64_string = data['image']  # Get the base64 string from the JSON
    try:
        image_data = base64.b64decode(base64_string)  # Decode the base64 string to binary data
    except ValueError:
        return jsonify(error="Invalid base64 string"), 400

    transcription = EssayService.perform_ocr(image_data)  # Pass the binary data to your OCR method
    if transcription:
        return jsonify(transcription=transcription)
    return jsonify(error="Could not transcribe image"), 400
