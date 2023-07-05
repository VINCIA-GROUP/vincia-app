import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/adaptive_question/page/adaptive_question_page.dart';
import 'package:http/http.dart' as http;
import 'package:vincia/modules/adaptive_question/page/controller/adaptive_question_controller.dart';
import 'package:vincia/modules/adaptive_question/services/adaptive_question_service.dart';

class AdaptiveQuestionModule extends Module {
  static const domain = String.fromEnvironment("AUTH0_DOMAIN");
  static const clientId = String.fromEnvironment("AUTH0_CLIENT_ID");

  @override
  List<Bind> get binds => [
        Bind((i) => Auth0(domain, clientId)),
        Bind((i) => http.Client()),
        Bind((i) => AdaptiveQuestionService(i(), i())),
        Bind((i) => AdaptiveQuestionController(i())),
      ];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (context, args) => const AdaptiveQuestionPage()),
      ];
}
