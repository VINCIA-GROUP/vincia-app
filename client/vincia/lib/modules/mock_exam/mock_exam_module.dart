import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/mock_exam/page/controller/mock_exam_controller.dart';
import 'package:vincia/modules/mock_exam/page/mock_exam_page.dart';
import 'package:http/http.dart' as http;
import 'package:vincia/modules/mock_exam/services/mock_exam_cache.dart';
import 'package:vincia/modules/mock_exam/services/mock_exam_service.dart';

class MockExamModule extends Module {
  static const domain = String.fromEnvironment("AUTH0_DOMAIN");
  static const clientId = String.fromEnvironment("AUTH0_CLIENT_ID");

  @override
  List<Bind> get binds => [
        Bind((i) => Auth0(domain, clientId)),
        Bind((i) => http.Client()),
        Bind((i) => MockExamCache),
        Bind((i) => MockExamQuestionService(i(), i())),
        Bind((i) => MockExamController(i())),
      ];

  @override
  List<ModularRoute> get routes => [
        ChildRoute('/', child: (context, args) => const MockExamPage()),
      ];
}
