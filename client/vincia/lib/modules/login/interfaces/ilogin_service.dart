import 'package:dartz/dartz.dart';

import '../models/errors.dart';
import '../models/success.dart';

abstract class ILoginService {
  Future<Either<Failure, Success>> login();
}
