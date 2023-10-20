import 'aplication_errors.dart';

class ConvertErrors {
  static Map<String, AplicationErrors> errors = {
    "1006": AplicationErrors.unauthorizedAccess,
    "2001": AplicationErrors.chaterro,
  };

  static AplicationErrors fromErroServer(String code) {
    var error = errors[code] ?? AplicationErrors.internalError;
    return error;
  }
}
