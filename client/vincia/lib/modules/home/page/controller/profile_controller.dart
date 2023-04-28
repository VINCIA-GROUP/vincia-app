import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:dartz/dartz.dart';
import 'package:mobx/mobx.dart';

import '../../interfaces/iauth_service.dart';

part 'profile_controller.g.dart';

class ProfileController = _ProfileController with _$ProfileController;

abstract class _ProfileController with Store {
  final IAuthService _authService;

  @observable
  UserProfile? user;

  _ProfileController(this._authService);

  @action
  Future init() async {
    var result = await _authService.getUserProfile();
    if (result.isRight()) {
      user = (result as Right).value;
    }
    return;
  }
}
