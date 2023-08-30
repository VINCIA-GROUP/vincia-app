import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';

import '../../interfaces/ihome_service.dart';

part 'home_controller.g.dart';

// ignore: library_private_types_in_public_api
class HomeController = _HomeController with _$HomeController;

abstract class _HomeController with Store {
  final IHomeService _homeService;

  @observable
  UserProfile? user;

  @observable
  int rating = 0;

  _HomeController(this._homeService);

  @action
  Future<void> init() async {
    var result = await _homeService.getUserProfile();

    if (result.isRight()) {
      user = (result as Right).value;
    }

    return;
  }

  Future<void> getRating() async {
    var abilityResult = await _homeService.getRating();
    if (abilityResult.isRight()) {
      rating = (abilityResult as Right).value;
    }
  }

  Future<void> menuFunction(String action) async {
    if (action == "logout") {
      var result = await _homeService.logout();
      if (result.isRight()) {
        Modular.to.navigate("/");
      }
      return;
    }
    if (action == "profile") {
      Modular.to.pushNamed("/profile");
      return;
    }
  }
}
