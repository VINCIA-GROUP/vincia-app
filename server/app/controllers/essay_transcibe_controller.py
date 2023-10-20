from flask import Flask, request, jsonify
from app import app
from app.services.essay_service import EssayService


@app.route("/api/essay/transcribe", methods=['POST'])
def transcribe_essay():
    print(request)
    if 'image' not in request.files:
        return jsonify(error="No file part"), 400
    file = request.files['image']
    if file.filename == '':
        return jsonify(error="No selected file"), 400
    if file:
        content = file.read()
        transcription = EssayService.perform_ocr(content)
        if transcription:
            return jsonify(transcription=transcription)
        return jsonify(error="Could not transcribe image"), 400
