import 'dart:convert';

import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:http/http.dart' as http;

import '../../../shared/errors/aplication_errors.dart';
import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';
import '../interfaces/ihome_service.dart';

class HomeService implements IHomeService {
  final Auth0 auth;
  final http.Client client;
  static const String apiUrl = String.fromEnvironment("API_URL");

  HomeService(this.auth, this.client);

  @override
  Future<Either<FailureModel, int>> getRating() async {
    try {
      final token = await getAcessToken();
      final response = await client.get(
        Uri.parse("$apiUrl/api/ability"),
        headers: {
          'Authorization': 'Bearer $token',
          'Accept': 'application/json',
          'Connection': 'Keep-Alive',
        },
      );
      if (response.statusCode == 200) {
        final body = jsonDecode(response.body)["data"];
        return Right(body['rating']);
      } else {
        final body = jsonDecode(response.body)["errors"];
        return Left(FailureModel.fromJson(body));
      }
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }

  @override
  Future<Either<FailureModel, SuccessModel>> logout() async {
    try {
      const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
      await auth.webAuthentication(scheme: scheme).logout();
      return Right(SuccessModel());
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }

  @override
  Future<Either<FailureModel, UserProfile>> getUserProfile() async {
    try {
      var credentials = await auth.credentialsManager.credentials();
      return Right(credentials.user);
    } catch (e) {
      return Left(FailureModel.fromEnum(AplicationErrors.internalError));
    }
  }

  Future<String> getAcessToken() async {
    var credentials = await auth.credentialsManager.credentials();
    return credentials.accessToken;
  }
}
