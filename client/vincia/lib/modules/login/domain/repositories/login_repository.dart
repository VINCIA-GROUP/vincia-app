import 'package:dartz/dartz.dart';
import 'package:vincia/modules/login/domain/entities/success.dart';

import '../../domain/errors/errors.dart';

abstract class LoginRepository {
  Future<Either<Failure, Success>> login();
}
