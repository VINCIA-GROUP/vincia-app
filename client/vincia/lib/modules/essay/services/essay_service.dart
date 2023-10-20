//lib/modules/essay/services/essay_service.dart

import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';
import 'dart:io';
import 'package:auth0_flutter/auth0_flutter.dart';

class TranscriptionService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  TranscriptionService(this.auth, this.client);

  Future<String?> transcribeImage(String imagePath) async {
    print('$apiUrl/api/essay/transcribe');
    final token = await getAccessToken();

    // Read the image file as a list of bytes.
    final imageBytes = File(imagePath).readAsBytesSync();

    // Convert the list of bytes to a base64 string.
    final base64String = base64Encode(imageBytes);

    try {
      final response = await client.post(
        Uri.parse('$apiUrl/api/essay/transcribe'),
        headers: {
          'Authorization': 'Bearer $token',
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'Connection': 'Keep-Alive',
        },
        body: jsonEncode({'image': base64String}),
      );

      if (response.statusCode == 200) {
        final Map<String, dynamic> data = jsonDecode(response.body);
        return data['transcription'];
      } else {
        print('Failed to transcribe image: ${response.reasonPhrase}');
        return null;
      }
    } on http.ClientException catch (e) {
      print('ClientException: $e');
      return null;
    } catch (e) {
      print('Error: $e');
      return null;
    }
  }

  Future<String> getAccessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }
}

class ImagePickerHandler {
  final ImagePicker _picker = ImagePicker();
  final TranscriptionService transcriptionService;

  ImagePickerHandler(this.transcriptionService);

  Future<String?> pickImage(BuildContext context) async {
    final XFile? image = await _picker.pickImage(source: ImageSource.camera);

    if (image != null) {
      final String imagePath = image.path;
      return await transcriptionService.transcribeImage(imagePath);
    }
  }
}
