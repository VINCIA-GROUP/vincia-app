//lib/modules/essay/essay_module.dart

import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/essay/page/essay_page.dart';
import 'package:vincia/modules/essay/page/essay_home_page.dart';
import 'package:vincia/modules/essay/page/essay_history_page.dart';
import 'package:vincia/modules/essay/page/essay_theme_page.dart';
import 'package:vincia/modules/essay/services/essay_history_service.dart';
import 'package:http/http.dart' as http;
import 'package:vincia/modules/essay/services/essay_theme_service.dart';
import 'controllers/essay_history_controller.dart';
import 'controllers/essay_theme_controller.dart';

class EssayModule extends Module {
  static const domain = String.fromEnvironment("AUTH0_DOMAIN");
  static const clientId = String.fromEnvironment("AUTH0_CLIENT_ID");

  @override
  List<Bind> get binds => [
    Bind((i) => Auth0(domain, clientId)),
    Bind((i) => http.Client()),
    Bind((i) => EssayHistoryService(i(), i())),
    Bind((i) => EssayHistoryController(i())),
    Bind((i) => EssayThemeService(i(), i())),
    Bind((i) => EssayThemeController(i())),
  ];

  @override
  List<ModularRoute> get routes => [
    ChildRoute('/', child: (context, args) => const EssayHomePage()),
    ChildRoute('/edit', child: (context, args) => EssayPage(
        selectedEssay: args.data,
        auth: Modular.get<Auth0>(),
        client: Modular.get<http.Client>(),
      ),
    ),
    ChildRoute('/history', child: (context, args) => const EssayHistoryPage()),
    ChildRoute('/theme', child: (context, args) => const EssayThemePage()),
  ];
}
