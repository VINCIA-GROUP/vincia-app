import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:vincia/shared/errors/aplication_errors.dart';
import 'package:vincia/shared/model/success_model.dart';
import '../../../shared/model/failure_model.dart';
import 'package:vincia/modules/question/model/question_model.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

import '../interfaces/iquestion_service.dart';

class QuestionService implements IQuestionService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  QuestionService(this.auth, this.client);

  @override
  Future<Either<FailureModel, QuestionModel>> getQuestion() async {
    try {
      final token = await getAcessToken();
      final response = await client.get(
        Uri.parse("$apiUrl/api/question"),
        headers: {
          'Authorization': 'Bearer $token',
          'Accept': 'application/json',
          'Connection': 'keep-alive',
        },
      );
      if (response.statusCode == 200) {
        final body = jsonDecode(response.body)["data"];
        return Right(QuestionModel.fromJson(body));
      } else {
        final body = jsonDecode(response.body)["errors"];
        return Left(FailureModel.fromJson(body));
      }
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }

  @override
  Future<Either<FailureModel, SuccessModel>> sendAnswerQuestion(
      String answer, Duration duration) async {
    try {
      final token = await getAcessToken();

      final Map<String, dynamic> requestData = {
        'answer': answer,
        'duration': duration.toString(),
      };

      var jsonData = jsonEncode(requestData);

      final response =
          await client.post(Uri.parse("$apiUrl/api/question/answer"),
              headers: {
                'Authorization': 'Bearer $token',
                'Content-Type': 'application/json',
              },
              body: jsonData);
      if (response.statusCode == 200) {
        return Right(SuccessModel());
      } else {
        final body = jsonDecode(response.body)["errors"];
        return Left(FailureModel.fromJson(body));
      }
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }

  Future<String> getAcessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }
}
