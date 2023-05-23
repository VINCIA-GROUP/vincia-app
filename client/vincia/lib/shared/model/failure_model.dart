import 'package:vincia/shared/errors/aplication_errors.dart';
import 'package:vincia/shared/errors/error_model.dart';
import 'package:vincia/shared/errors/table_convert_errors.dart';

class FailureModel implements Exception {
  List<ErrorModel> errors = [];

  FailureModel(ErrorModel error) {
    errors.add(error);
  }

  FailureModel.fromListErrors(this.errors);

  FailureModel.fromEnum(AplicationErrors error) {
    errors.add(ErrorModel.fromEnum(error));
  }

  factory FailureModel.fromJson(List<dynamic> json) {
    var errorsList = json
        .map((errorJson) => ConvertErrors.fromErroServer(errorJson["code"]))
        .toList();
    List<ErrorModel> errors =
        errorsList.map((e) => ErrorModel.fromEnum(e)).toList();
    return FailureModel.fromListErrors(errors);
  }
}
