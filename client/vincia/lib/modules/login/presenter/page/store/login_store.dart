import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';
import 'package:vincia/modules/login/presenter/page/store/state/login_state.dart';

import '../../../domain/usercases/login.dart';

part 'login_store.g.dart';

class LoginStore = _LoginStore with _$LoginStore;

abstract class _LoginStore with Store {
  final Login login;

  _LoginStore(this.login);

  @observable
  LoginState state = InitialState();

  @action
  void onPressedLogin() async {
    state = LodingSate();
    var result = await login();
    if (result.isRight()) {
      Modular.to.navigate("/home");
      state = InitialState();
    }
    if (result.isLeft()) {
      state = FailureSate();
    } else {
      state = InitialState();
    }
  }
}
