import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';

import '../models/errors.dart';
import '../models/success.dart';

abstract class IAuthService {
  Future<Either<Failure, Success>> logout();
  Future<Either<Failure, UserProfile>> getUserProfile();
}
