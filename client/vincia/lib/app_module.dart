import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/login/infra/repositories/login_repository_impl.dart';
import 'package:vincia/modules/login/presenter/page/store/login_store.dart';

import 'modules/Initial/presenter/page/initial_page.dart';
import 'modules/home/presenter/page/home_page.dart';
import 'modules/login/domain/usercases/login.dart';
import 'modules/login/external/datasources/authzero_datasource.dart';
import 'modules/login/presenter/page/login_page.dart';

class AppModule extends Module {
  static const domain = String.fromEnvironment("AUTH0_DOMAIN");
  static const clientId = String.fromEnvironment("AUTH0_CLIENT_ID");

  @override
  List<Bind> get binds => [
        Bind((i) => Auth0(domain, clientId)),
        Bind((i) => AuthzeroDatasourceImpl(i())),
        Bind((i) => LoginRepositoryImpl(i())),
        Bind((i) => LoginImpl(i())),
        Bind((i) => LoginStore(i()))
      ];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (context, args) => InitialPage()),
        ChildRoute('/home', child: (context, args) => HomePage()),
        ChildRoute('/login', child: (context, args) => LoginPage()),
      ];
}
