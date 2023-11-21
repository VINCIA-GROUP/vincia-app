// lib/modules/essay/services/essay_analysis_service.dart
import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class EssayAnalysisService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  EssayAnalysisService(this.auth, this.client);

  Future<Map<String, dynamic>> analyzeEssay(essayData) async {
    print(essayData);
    final token = await getAcessToken();
    final response = await client.post(
      Uri.parse('$apiUrl/api/essay/analysis'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Connection': 'Keep-Alive',
      },
      body: jsonEncode(essayData),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      print('Response body: ${response.body}'); // Add this line
      throw Exception('Failed to analyze essay: ${response.body}');
    }
  }

  Future<String> getAcessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }
}
