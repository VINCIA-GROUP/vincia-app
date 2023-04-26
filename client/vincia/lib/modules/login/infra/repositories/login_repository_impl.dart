import 'package:dartz/dartz.dart';
import 'package:vincia/modules/login/domain/entities/success.dart';
import 'package:vincia/modules/login/infra/datasources/login_datasource.dart';

import '../../domain/errors/errors.dart';
import '../../domain/repositories/login_repository.dart';

class LoginRepositoryImpl extends LoginRepository {
  final AuthzeroDatasource authzeroDatasource;

  LoginRepositoryImpl(this.authzeroDatasource);

  @override
  Future<Either<Failure, Success>> login() async {
    try {
      await authzeroDatasource.login();
      return Right(Success());
    } catch (e) {
      return Left(Failure());
    }
  }
}
