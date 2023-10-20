import 'dart:convert';
import 'package:dartz/dartz.dart';
import 'package:http/http.dart' as http;
import 'package:vincia/shared/errors/aplication_errors.dart';
import 'package:vincia/shared/model/failure_model.dart';
import '../interfaces/i_essay_theme_service.dart';
import 'package:auth0_flutter/auth0_flutter.dart';
import '../models/essay_theme_model.dart';

class EssayThemeService implements IEssayThemeService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  // Define the private variable to store the list of essays
  List<EssayTheme> _essaythemes = [];

  EssayThemeService(this.auth, this.client);

  List<EssayTheme> get essaythemes => _essaythemes;

  Future<List<EssayTheme>> getEssayTheme() async {
    final token = await getAcessToken();
    final response = await client.get(
      Uri.parse('$apiUrl/api/essay/theme'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/json',
        'Connection': 'Keep-Alive',
      },
    );

    if (response.statusCode == 200) {
      Map<String, dynamic> decodedResponse = jsonDecode(response.body);
      if (decodedResponse.containsKey('data') &&
          decodedResponse['data'] is List) {
        _essaythemes = (decodedResponse['data'] as List)
            .map((dynamic item) => EssayTheme.fromJson(item))
            .toList();
      } else {
        throw FormatException('Unexpected response format');
      }

      return _essaythemes;
    } else {
      throw Exception('Failed to fetch essay themes');
    }
  }

  Future<List<EssayTheme>> getRandomEssayTheme() async {
    final token = await getAcessToken();
    final response = await client.get(
      Uri.parse('$apiUrl/api/essay/theme/random'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/json',
        'Connection': 'Keep-Alive',
      },
    );

    if (response.statusCode == 200) {
      Map<String, dynamic> decodedResponse = jsonDecode(response.body);
      if (decodedResponse.containsKey('data') &&
          decodedResponse['data'] is List) {
        _essaythemes = (decodedResponse['data'] as List)
            .map((dynamic item) => EssayTheme.fromJson(item))
            .toList();
      } else {
        throw FormatException('Unexpected response format');
      }

      return _essaythemes;
    } else {
      throw Exception('Failed to fetch essay themes');
    }
  }

  Future<String> getUserId() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.user.sub;
  }

  Future<String> getAcessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }
}
