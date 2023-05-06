import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';

import '../interfaces/ilogin_service.dart';
import '../models/errors.dart';
import '../models/success.dart';

class LoginService implements ILoginService {
  final Auth0 auth;

  LoginService(this.auth);

  @override
  Future<Either<Failure, Success>> login() async {
    try {
      const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
      var cre = await auth
          .webAuthentication(scheme: scheme)
          .login(audience: "vincia-api-v1");
      return Right(Success());
    } catch (e) {
      return Left(Failure());
    }
  }
}
