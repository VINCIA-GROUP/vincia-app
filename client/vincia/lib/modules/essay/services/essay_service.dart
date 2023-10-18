//lib/modules/essay/services/essay_service.dart

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';


class TranscriptionService {
  final String apiUrl;

  TranscriptionService(this.apiUrl);

  Future<String?> transcribeImage(String imagePath) async {
    final request = http.MultipartRequest(
      'POST',
      Uri.parse('$apiUrl/essay/transcribe'),  // Endpoint
    );

    request.files.add(
      await http.MultipartFile.fromPath(
        'image',
        imagePath,
      ),
    );

    try {
      final response = await request.send();

      if (response.statusCode == 200) {
        final responseBody = await response.stream.bytesToString();
        final Map<String, dynamic> data = jsonDecode(responseBody);
        return data['transcription'];
      } else {
        print('Failed to transcribe image: ${response.reasonPhrase}');
      }
    } catch (e) {
      print('Error: $e');
    }
  }
}


class ImagePickerHandler {
  final ImagePicker _picker = ImagePicker();
  final String apiUrl;

  ImagePickerHandler(this.apiUrl);

  Future<String?> pickImage(BuildContext context) async {
    final XFile? image = await _picker.pickImage(source: ImageSource.camera);

    if (image != null) {
      final String imagePath = image.path;
      return await TranscriptionService(apiUrl).transcribeImage(imagePath);
    }
  }
}