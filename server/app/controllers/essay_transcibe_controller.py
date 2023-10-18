# from flask import jsonify, request, session
# from app import app
# from app.decorator.requires_auth import requires_auth
# from app.controllers.base_controller import *
# from app.domain.errors import api_exception
# from app.domain.errors.authentication_errors import AuthorizationHeaderMissing
# import pytesseract
# from PIL import Image
# import io

# @app.route("/api/essay/transcribe", endpoint="essay/transcribe", methods=['POST'])
# def transcribe():
#     print("Entrou na função")
#     if 'image' not in request.files:
#         return jsonify({'error': 'No image provided.'}), 400
    
#     image_file = request.files['image']
#     image = Image.open(io.BytesIO(image_file.read()))
    
#     text = pytesseract.image_to_string(image)
    
#     return jsonify({'text': text})


from flask import Flask, request, jsonify
from app import app
from app.services.essay_service import EssayService


@app.route("/api/essay/transcribe", methods=['POST'])
def transcribe_essay():
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
