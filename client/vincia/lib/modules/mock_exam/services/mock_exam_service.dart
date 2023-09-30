import 'dart:convert';

import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:sqflite/utils/utils.dart';
import 'package:vincia/modules/mock_exam/interfaces/i_mock_exam_service.dart';

import 'package:http/http.dart' as http;
import 'package:vincia/modules/mock_exam/model/mock_exam_answer_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_areas_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_cache_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';
import 'package:vincia/modules/mock_exam/services/mock_exam_cache.dart';
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

  @override
  Future<Either<FailureModel, MockExamAreasModel>> getQuestions() async {
    try {
      final cache = await mockExamCache.database;
      MockExamAreasModel result = MockExamAreasModel([], [], [], []);
      final hasData = firstIntValue(await cache.rawQuery('SELECT COUNT(*) FROM mock_exam'))! > 0;
      if (hasData) {
        final List<Map<String, dynamic>> questions = await cache.query('mock_exam');
        for (var question in questions) {
          MockExamCacheModel q = MockExamCacheModel.fromMap(question);
          if (q.area == "natural_science") result.naturalScience.add(q.toQuestion());
          if (q.area == "humanities") result.humanities.add(q.toQuestion());
          if (q.area == "mathematics") result.mathematics.add(q.toQuestion());
          if (q.area == "languages") result.languages.add(q.toQuestion());
        }
        return Right(result);
      } else {
        final areas = await getQuestionsFromAPI();
        return areas.fold(
          (failure) {
            return Left(FailureModel.fromEnum(AplicationErrors.internalError));
          },
          (areas) async {
            for (MockExamQuestionModel questions in areas.naturalScience) {
              MockExamCacheModel q = questions.toCache("natural_science", Duration.zero, "");
              await mockExamCache.insert(q.toMap());
            }
            for (MockExamQuestionModel questions in areas.humanities) {
              MockExamCacheModel q = questions.toCache("humanities", Duration.zero, "");
              await mockExamCache.insert(q.toMap());
            }
            for (MockExamQuestionModel questions in areas.languages) {
              MockExamCacheModel q = questions.toCache("languges", Duration.zero, "");
              await mockExamCache.insert(q.toMap());
            }
            for (MockExamQuestionModel questions in areas.mathematics) {
              MockExamCacheModel q = questions.toCache("mathematics", Duration.zero, "");
              await mockExamCache.insert(q.toMap());
            }
            return Right(areas);
          });
      }
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    } 
  }

  // @override
  // Future<Either<FailureModel, SuccessModel>> saveQuestionState(MockExamQuestionModel question, MockExamAnswerModel answer) async {
  //   try {

  //   } catch (e) {
  // 
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