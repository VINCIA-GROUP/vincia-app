// lib/modules/essay/services/essay_history_service_impl.dart

import 'dart:convert';
import 'package:http/http.dart' as http;
import '../interfaces/i_essay_history_service.dart';
import '../models/essay_model.dart';
import 'package:auth0_flutter/auth0_flutter.dart';

class EssayHistoryServiceImpl implements IEssayHistoryService {
  final Auth0 auth;
  final String apiUrl;

  EssayHistoryServiceImpl(this.auth, this.apiUrl);

  Future<List<Essay>> getEssayHistory() async {
    final userId = await getUserId();
    final response = await http.get(
      Uri.parse('$apiUrl/api/essay/history/$userId'));

    if (response.statusCode == 200) {
      List<dynamic> body = jsonDecode(response.body);
      List<Essay> essays = body.map((dynamic item) => Essay.fromJson(item)).toList();
      return essays;
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
