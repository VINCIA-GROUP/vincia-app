import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';

import '../interfaces/iauth_service.dart';
import '../models/errors.dart';
import '../models/success.dart';

class AuthService implements IAuthService {
  final Auth0 auth;

  AuthService(this.auth);

  @override
  Future<Either<Failure, Success>> logout() async {
    try {
      const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
      await auth.webAuthentication(scheme: scheme).logout();
      return Right(Success());
    } catch (e) {
      return Left(Failure());
    }
  }

  Future<Either<Failure, UserProfile>> getUserProfile() async {
    try {
      var credentials = await auth.credentialsManager.credentials();
      return Right(credentials.user);
    } catch (e) {
      return Left(Failure());
    }
  }
}
