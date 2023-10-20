import 'dart:convert';
import 'package:http/http.dart' as http;
import '../interfaces/i_essay_history_service.dart';
import '../models/essay_model.dart';
import 'package:auth0_flutter/auth0_flutter.dart';

class EssayHistoryServiceImpl implements IEssayHistoryService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  // Define the private variable to store the list of essays
  List<Essay> _essays = [];

  EssayHistoryServiceImpl(this.auth, this.client);

  List<Essay> get essays => _essays;

  @override
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

  @override
  Future<List<Essay>> getUnfinishedEssay() async {
    final token = await getAcessToken();
    final response = await client.get(
        Uri.parse('$apiUrl/api/essay/unfinished'),
        headers: {
          'Authorization': 'Bearer $token',
          'Accept': 'application/json',
          'Connection': 'Keep-Alive',
        },
    );

    if (response.statusCode == 200) {
      List<dynamic> body = jsonDecode(response.body);

      // Update the _essays variable with the fetched essays
      _essays = body.map((dynamic item) => Essay.fromJson(item)).toList();

      return _essays;
    } else {
      throw Exception('Failed to fetch unfinished essay');
    }
  }

  @override
  Future<Essay> createEssay(Map<String, dynamic> essayData) async {
    final token = await getAcessToken();
    final response = await client.post(
      Uri.parse('$apiUrl/api/essay/create'),
      headers: {
        'Authorization': 'Bearer $token',
        'Accept': 'application/json',
        'Connection': 'Keep-Alive',
      },
      body: jsonEncode(essayData),
    );

    if (response.statusCode == 201) {
      Map<String, dynamic> body = jsonDecode(response.body);
      final Essay newEssay = Essay.fromJson(body);
      return newEssay;
    } else {
      throw Exception('Failed to create essay');
    }
  }


  @override
  Future<String> getUserId() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.user.sub;
  }

  Future<String> getAcessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }
}