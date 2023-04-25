import 'package:auth0_flutter/auth0_flutter.dart';

class LoginService {
  late Auth0 auth0;

  LoginService(this.auth0);

  Future login() async {
    await auth0.webAuthentication().login();
  }
}
