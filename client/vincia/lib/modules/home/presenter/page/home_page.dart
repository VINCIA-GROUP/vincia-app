import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Row(
            children: [
              const Padding(
                padding: EdgeInsets.all(8.0),
                child: Image(
                  width: 40,
                  height: 40,
                  image: AssetImage("assets/images/logo-img.png"),
                ),
              ),
              Text(
                "Vincia",
                style: TextStyle(
                    fontSize: 28,
                    color: Theme.of(context).colorScheme.primary,
                    fontFamily: 'BirthstoneBounce'),
              ),
            ],
          ),
          actions: [
            Padding(
              padding: EdgeInsets.all(8.0),
              child: CircleAvatar(
                child: Image(
                    image: AssetImage("assets/images/avatar_default.png")),
              ),
            )
          ],
        ),
        body: Column(
          children: [
            FloatingActionButton(
              heroTag: "b",
              onPressed: () async {
                var auth = Modular.get<Auth0>();
                const scheme = String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
                await auth.webAuthentication(scheme: scheme).logout();
                Modular.to.navigate("/");
              },
              child: const Icon(Icons.access_time_sharp),
            ),
            Padding(
              padding: const EdgeInsets.all(8),
              child: FloatingActionButton(
                heroTag: "a",
                onPressed: () async {
                  //var auth = Modular.get<Auth0>();
                  Modular.to.navigate("/");
                },
                child: const Icon(Icons.abc_outlined),
              ),
            )
          ],
        ));
  }
}
