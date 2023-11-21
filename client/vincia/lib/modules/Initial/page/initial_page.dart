import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

class InitialPage extends StatelessWidget {
  InitialPage({super.key}) {
    var auth = Modular.get<Auth0>();
    auth.credentialsManager.hasValidCredentials().then((value) => {
          if (value)
            {Modular.to.navigate("/home")}
          else
            {Modular.to.navigate("/login")}
        });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(child: Image.asset("assets/images/logo-img.png")),
    );
  }
}

