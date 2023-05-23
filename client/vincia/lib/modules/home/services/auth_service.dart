import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';

import '../../../shared/errors/error_model.dart';
import '../interfaces/iauth_service.dart';
import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';

class AuthService implements IAuthService {
  final Auth0 auth;

  AuthService(this.auth);

  @override
  Future<Either<FailureModel, SuccessModel>> logout() async {
    try {
      const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
      await auth.webAuthentication(scheme: scheme).logout();
      return Right(SuccessModel());
    } catch (e) {
      //TODO: alterar error
      return Left(FailureModel(ErrorModel("2", "Erro ao efetuar o logout")));
    }
  }

  @override
  Future<Either<FailureModel, UserProfile>> getUserProfile() async {
    try {
      var credentials = await auth.credentialsManager.credentials();
      return Right(credentials.user);
    } catch (e) {
      //TODO: alterar error
      return Left(
          FailureModel(ErrorModel("1", "Erro ao obter as credenciais")));
    }
  }
}
