import 'aplication_errors.dart';

class ErrorModel {
  late String code;
  late String message;

  ErrorModel(this.code, this.message);

  ErrorModel.fromEnum(AplicationErrors enumValue) {
    code = enumValue.code;
    message = enumValue.message;
  }

  factory ErrorModel.fromJson(Map<String, dynamic> json) {
    return ErrorModel(
      json['code'] as String,
      json['message'] as String,
    );
  }
}
