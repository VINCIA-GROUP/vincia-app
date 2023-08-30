import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';

abstract class IHomeService {
  Future<Either<FailureModel, int>> getRating();
  Future<Either<FailureModel, SuccessModel>> logout();
  Future<Either<FailureModel, UserProfile>> getUserProfile();
}
