import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:vincia/shared/errors/error_model.dart';

import '../interfaces/ilogin_service.dart';
import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';

class LoginService implements ILoginService {
  final Auth0 auth;

  LoginService(this.auth);

  @override
  Future<Either<FailureModel, SuccessModel>> login() async {
    try {
      const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
      var credentials = await auth
          .webAuthentication(scheme: scheme)
          .login(audience: "vincia-api-v1");
      return Right(SuccessModel());
    } catch (e) {
      //TODO: alterar error
      return Left(FailureModel(ErrorModel("3", "Erro ao efetuar o login.")));
    }
  }
}
