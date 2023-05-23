import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';

import '../../interfaces/iauth_service.dart';

part 'home_controller.g.dart';

class HomeController = _HomeController with _$HomeController;

abstract class _HomeController with Store {
  final IAuthService _authService;

  @observable
  UserProfile? user;

  _HomeController(this._authService);

  @action
  Future<void> init() async {
    var result = await _authService.getUserProfile();
    if (result.isRight()) {
      user = (result as Right).value;
    }
    return;
  }

  Future<void> menuFunction(String action) async {
    if (action == "logout") {
      var result = await _authService.logout();
      if (result.isRight()) {
        Modular.to.navigate("/");
      }
      return;
    }
    if (action == "profile") {
      Modular.to.navigate("/profile");
      return;
    }
  }
}
