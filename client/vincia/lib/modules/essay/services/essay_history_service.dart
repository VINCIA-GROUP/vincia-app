import 'dart:convert';
import 'package:http/http.dart' as http;
import '../interfaces/i_essay_history_service.dart';
import '../models/essay_model.dart';
import 'package:auth0_flutter/auth0_flutter.dart';

class EssayHistoryService implements IEssayHistoryService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  // Define the private variable to store the list of essays
  List<Essay> _essays = [];

  EssayHistoryService(this.auth, this.client);

  List<Essay> get essays => _essays;

  Future<List<Essay>> getEssayHistory() async {
    final userId = await getUserId();
    final response = await client.get(
        Uri.parse('$apiUrl/api/essay/history/$userId'));

    if (response.statusCode == 200) {
      List<dynamic> body = jsonDecode(response.body);

      // Update the _essays variable with the fetched essays
      _essays = body.map((dynamic item) => Essay.fromJson(item)).toList();

      return _essays;
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
