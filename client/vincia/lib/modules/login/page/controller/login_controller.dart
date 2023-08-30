import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';
import 'package:vincia/modules/login/page/controller/state/login_state.dart';

import '../../interfaces/ilogin_service.dart';

part 'login_controller.g.dart';

// ignore: library_private_types_in_public_api
class LoginController = _LoginController with _$LoginController;

abstract class _LoginController with Store {
  final ILoginService loginService;

  _LoginController(this.loginService);

  @observable
  LoginState state = InitialState();

  @action
  Future<void> login() async {
    state = LodingState();
    var result = await loginService.login();
    if (result.isRight()) {
      Modular.to.navigate("/home");
      state = InitialState();
    }
    if (result.isLeft()) {
      state = FailureState();
    } else {
      state = InitialState();
    }
  }
}
