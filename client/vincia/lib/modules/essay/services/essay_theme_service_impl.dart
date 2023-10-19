// lib/modules/essay/services/essay_history_service_impl.dart

import 'dart:convert';
import 'package:http/http.dart' as http;
import '../interfaces/i_essay_theme_service.dart';
import 'package:auth0_flutter/auth0_flutter.dart';
import '../models/essay_theme_model.dart';

class EssayThemeServiceImpl implements IEssayThemeService {
  final Auth0 auth;
  final String apiUrl;

  EssayThemeServiceImpl(this.auth, this.apiUrl);

  Future<List<EssayTheme>> getEssayTheme() async {
    final userId = await getUserId();
    final response = await http.get(
      Uri.parse('$apiUrl/api/essay/theme/$userId'));

    if (response.statusCode == 200) {
      List<dynamic> body = jsonDecode(response.body);
      List<EssayTheme> essaytheme = body.map((dynamic item) => EssayTheme.fromJson(item)).toList();
      return essaytheme;
    } else {
      throw Exception('Failed to fetch essay history');
    }
  }

  Future<List<EssayTheme>> getRandomEssayTheme() async {
    final userId = await getUserId();
    final response = await http.get(
      Uri.parse('$apiUrl/api/essay/theme/random/$userId'));

    if (response.statusCode == 200) {
      List<dynamic> body = jsonDecode(response.body);
      List<EssayTheme> essaytheme = body.map((dynamic item) => EssayTheme.fromJson(item)).toList();
      return essaytheme;
    } else {
      throw Exception('Failed to fetch essay history');
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
