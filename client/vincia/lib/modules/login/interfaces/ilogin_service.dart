import 'package:dartz/dartz.dart';

import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';

abstract class ILoginService {
  Future<Either<FailureModel, SuccessModel>> login();
}
