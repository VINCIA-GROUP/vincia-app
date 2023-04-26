import 'package:dartz/dartz.dart';
import 'package:vincia/modules/login/domain/entities/success.dart';
import 'package:vincia/modules/login/domain/repositories/login_repository.dart';

import '../errors/errors.dart';

abstract class Login {
  Future<Either<Failure, Success>> call();
}

class LoginImpl implements Login {
  final LoginRepository loginRepository;

  LoginImpl(this.loginRepository);

  Future<Either<Failure, Success>> call() {
    return loginRepository.login();
  }
}
