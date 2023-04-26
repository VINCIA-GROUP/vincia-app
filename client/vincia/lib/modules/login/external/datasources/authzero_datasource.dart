import 'package:auth0_flutter/auth0_flutter.dart';

import '../../infra/datasources/login_datasource.dart';

class AuthzeroDatasourceImpl extends AuthzeroDatasource {
  final Auth0 auth;

  AuthzeroDatasourceImpl(this.auth);

  @override
  Future login() async {
    const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
    await auth.webAuthentication(scheme: scheme).login();
  }
}
