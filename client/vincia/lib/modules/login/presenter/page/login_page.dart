import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:vincia/modules/login/presenter/page/store/login_store.dart';
import 'package:vincia/modules/login/presenter/page/store/state/login_state.dart';

class LoginPage extends StatelessWidget {
  final LoginStore loginStore = Modular.get<LoginStore>();
  final _scaffoldKey = GlobalKey<ScaffoldState>();

  LoginPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Padding(
              padding: EdgeInsets.all(30.0),
              child: Image(
                image: AssetImage("assets/images/logo-img.png"),
              ),
            ),
            Observer(builder: (context) {
              if (loginStore.state is LodingSate) {
                return const CircularProgressIndicator();
              }
              if (loginStore.state is FailureSate) {
                WidgetsBinding.instance.addPostFrameCallback((_) {
                  ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                    content: Text(
                        "Erro ao tentar efetuar o login. Por favor tente novamente mais tarde."),
                  ));
                });
              }
              return _buttonLogin(
                  context, "Log in", () => loginStore.onPressedLogin());
            }),
          ],
        ),
      ),
    );
  }

  Widget _buttonLogin(BuildContext context, String text, Function() onPressed) {
    final TextStyle textButtonStyle = TextStyle(
        fontSize: 16,
        fontWeight: FontWeight.bold,
        color: Theme.of(context).colorScheme.onPrimary);
    final ButtonStyle buttonStyle = ElevatedButton.styleFrom(
        textStyle: const TextStyle(fontSize: 20),
        backgroundColor: Theme.of(context).colorScheme.primary);
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: ConstrainedBox(
        constraints: const BoxConstraints(
          minHeight: 45,
          minWidth: 100,
        ),
        child: ElevatedButton(
            style: buttonStyle,
            onPressed: onPressed,
            child: Text(
              text,
              style: textButtonStyle,
            )),
      ),
    );
  }
}
