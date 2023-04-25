import 'package:flutter_modular/flutter_modular.dart';

import 'modules/Initial/presenter/page/initial_page.dart';
import 'modules/home/presenter/page/home_page.dart';
import 'modules/login/presenter/page/login_page.dart';

class AppModule extends Module {
  @override
  List<Bind> get binds => [];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (context, args) => InitialPage()),
        ChildRoute('/home', child: (context, args) => HomePage()),
        ChildRoute('/login', child: (context, args) => LoginPage()),
      ];
}
