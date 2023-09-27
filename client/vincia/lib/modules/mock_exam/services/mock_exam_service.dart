import 'dart:convert';

import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:vincia/modules/mock_exam/interfaces/i_mock_exam_service.dart';

import 'package:http/http.dart' as http;
import 'package:vincia/modules/mock_exam/model/mock_exam_answer_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_areas_model.dart';
// import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';
import 'package:vincia/shared/errors/aplication_errors.dart';
import 'package:vincia/shared/model/failure_model.dart';
import 'package:vincia/shared/model/success_model.dart';

class MockExamQuestionService implements IMockExamService {
  final Auth0 auth;
  final http.Client client;
  final MockExamCache mockExamCache = MockExamCache.instance;
  static const String apiUrl = String.fromEnvironment("API_URL");

  MockExamQuestionService(this.auth, this.client);

  @override
  Future<String> getAcessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }

  @override
  Future<String> getUserId() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.user.sub;
  }

  @override
  Future<Either<FailureModel, MockExamAreasModel>> getQuestionsFromAPI() async {
    try {
      final token = await getAcessToken();
      final response = await client.get(
        Uri.parse("$apiUrl/api/mock-exam/questions"),
        headers: {
          'Authorization': 'Bearer $token',
          'Accept': 'application/json',
          'Connection': 'Keep-Alive'
        }
      );
      if (response.statusCode == 200) {
        final body = jsonDecode(response.body)["data"];
        return Right(MockExamAreasModel.fromJson(body));
      } else {
        final body = jsonDecode(response.body)["errors"];
        return Left(FailureModel.fromJson(body));
      }
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }

  Future<void> getQuestions() async {
    final cache = await MockExamCache.database;
    final tableExists = await cache.query(
      'sqlite_master',
      where: 'name = ?', 
      whereArgs: ['mock_exam']
    );
    if (tableExists.isEmpty) { //cria tabela, pega dados da api e coloca na tabela //NAO ESQUECER DE TRANSFORMAR NO MODELO CRIADO PARA O CACHE
      await mockExamCache._createTable(cache, 1);
      final questions = await getQuestionsFromAPI();
      for (var question in questions) {
        await mockExamCache.insert(question);
      }
      return questions
    } else { //pega questões da tabela //NAO ESQUECER DE TRANSFORMAR NO MODELO CRIADO PARA O CACHE
      final questions = await cache.query('mock_exam');
      return questions
    }
  }

  

  // @override
  // Future<Either<FailureModel, SuccessModel>> saveQuestionState(MockExamQuestionModel question, MockExamAnswerModel answer) async {
  //   try {

  //   }
  // }

  @override
  Future<Either<FailureModel, SuccessModel>> sendMockExamAnswer(List<MockExamAnswerModel> answers) async {
    try {
      final token = await getAcessToken();

      var answersJson = answers.map((answer) {
        jsonEncode(answer.toJson());
      }).toList();
      
      final response = await client.post(Uri.parse("$apiUrl/api/mock-exam/submmit"),
        headers: {
          'Authorization': 'Bearer $token',
          'Content-Type': 'application/json',
        },
        body: answersJson
      );

      if (response.statusCode == 200) {
        final body = jsonDecode(response.body)["data"];
        return Right(body);
      } else {
        final body = jsonDecode(response.body)["errors"];
        return Left(FailureModel.fromJson(body));
      }

    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }
}