import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:mobx/mobx.dart';

import '../../interfaces/ihome_service.dart';

part 'profile_controller.g.dart';

// ignore: library_private_types_in_public_api
class ProfileController = _ProfileController with _$ProfileController;

abstract class _ProfileController with Store {
  final IHomeService _homeService;

  @observable
  UserProfile? user;

  _ProfileController(this._homeService);

  @action
  Future<void> init() async {
    var result = await _homeService.getUserProfile();
    if (result.isRight()) {
      user = (result as Right).value;
    }
    return;
  }
}
