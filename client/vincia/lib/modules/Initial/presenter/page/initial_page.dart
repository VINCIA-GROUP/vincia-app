import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

class InitialPage extends StatelessWidget {
  InitialPage({super.key}) {
    Future.delayed(
        const Duration(seconds: 2), () => {Modular.to.navigate("/login")});
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(child: Image.asset("assets/images/logo-img.png")),
    );
  }
}
