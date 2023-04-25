import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia_app/app_module.dart';
import 'package:vincia_app/app_widget.dart';

void main() {
  runApp(ModularApp(
    module: AppModule(),
    child: AppWidget(),
  ));
}
