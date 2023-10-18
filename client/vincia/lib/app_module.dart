import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/adaptive_question/adaptive_question_module.dart';
import 'package:vincia/modules/home/services/home_service.dart';
import 'package:vincia/modules/login/services/login_service.dart';
import 'package:http/http.dart' as http;
import 'modules/Initial/page/initial_page.dart';
import 'modules/essay/essay_module.dart';
import 'modules/home/page/controller/home_controller.dart';
import 'modules/home/page/controller/profile_controller.dart';
import 'modules/home/page/home_page.dart';
import 'modules/home/page/profile_page.dart';
import 'modules/login/page/controller/login_controller.dart';
import 'modules/login/page/login_page.dart';

class AppModule extends Module {
  static const domain = String.fromEnvironment("AUTH0_DOMAIN");
  static const clientId = String.fromEnvironment("AUTH0_CLIENT_ID");

  @override
  List<Bind> get binds => [
        Bind((i) => Auth0(domain, clientId)),
        Bind((i) => http.Client()),
        Bind((i) => LoginService(i())),
        Bind((i) => HomeService(i(), i())),
        Bind((i) => LoginController(i())),
        Bind((i) => HomeController(i())),
        Bind((i) => ProfileController(i())),
      ];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (context, args) => InitialPage()),
        ChildRoute('/home', child: (context, args) => HomePage()),
        ChildRoute('/login', child: (context, args) => LoginPage()),
        ModuleRoute('/question', module: AdaptiveQuestionModule()),
        ChildRoute('/profile', child: (context, args) => ProfilePage()),
        ModuleRoute('/essay', module: EssayModule()),
        ModuleRoute('/essay/edit', module: EssayModule()),
      ];
}
