import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  static const List<String> list = <String>['One', 'Two', 'Three', 'Four'];

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
              padding: const EdgeInsets.all(4.0),
              child: Container(
                padding: const EdgeInsets.symmetric(horizontal: 5),
                decoration: BoxDecoration(
                  border: Border.all(width: 1),
                  borderRadius: const BorderRadius.all(Radius.circular(8)),
                ),
                child: Row(
                  children: [
                    const Text(
                      "1255",
                    ),
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.center,
                      children: const [
                        Icon(
                          Icons.arrow_drop_up,
                          color: Colors.green,
                        ),
                        Text(
                          "20",
                          style: TextStyle(
                              color: Colors.green,
                              fontWeight: FontWeight.bold,
                              fontSize: 10),
                        ),
                      ],
                    )
                  ],
                ),
              ),
            ),
            PopupMenuButton(
              icon: Row(
                children: const [
                  CircleAvatar(
                    child: Image(
                        image: AssetImage("assets/images/avatar_default.png")),
                  ),
                  Icon(Icons.arrow_drop_down_sharp)
                ],
              ),
              itemBuilder: (BuildContext context) {
                return const <PopupMenuEntry>[
                  PopupMenuItem(
                    value: 1,
                    child: Text('Opção 1'),
                  ),
                  PopupMenuItem(
                    value: 2,
                    child: Text('Opção 2'),
                  ),
                  PopupMenuItem(
                    value: 3,
                    child: Text('Log out'),
                  ),
                ];
              },
              onSelected: (value) {
                // Aqui você pode fazer algo quando uma opção for selecionada
                print('Opção selecionada: $value');
              },
            ),
          ],
        ),
        body: Column(
          children: [
            Expanded(child: Container()),
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 16.0),
              child: Container(
                constraints: const BoxConstraints(
                  maxHeight: 110,
                ),
                child: ListView(
                  scrollDirection: Axis.horizontal,
                  children: [
                    _carouselButton(
                      "Questões",
                      Icons.checklist_rtl,
                      () {
                        Modular.to.navigate("/question");
                      },
                    ),
                    _carouselButton(
                      "Simulado",
                      Icons.ballot_sharp,
                      () {},
                    ),
                    _carouselButton(
                      "Redação",
                      Icons.create,
                      () {},
                    ),
                    _carouselButton(
                      "Estatisticas",
                      Icons.stacked_bar_chart_outlined,
                      () {},
                    ),
                    _carouselButton(
                      "Test log out",
                      Icons.logout,
                      () async {
                        var auth = Modular.get<Auth0>();
                        const scheme =
                            String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
                        await auth.webAuthentication(scheme: scheme).logout();
                        Modular.to.navigate("/");
                      },
                    ),
                    _carouselButton(
                      "Test return init",
                      Icons.login,
                      () async {
                        Modular.to.navigate("/");
                      },
                    ),
                  ],
                ),
              ),
            )
          ],
        ));
  }

  Widget _carouselButton(String text, IconData icon, Function() onPressed) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
          return SizedBox(
            width: constraints.maxHeight,
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Theme.of(context).colorScheme.primaryContainer,
                foregroundColor:
                    Theme.of(context).colorScheme.onPrimaryContainer,
                shape: const RoundedRectangleBorder(
                  borderRadius: BorderRadius.all(Radius.circular(10.0)),
                ),
              ),
              onPressed: onPressed,
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(icon),
                  const SizedBox(
                    height: 5,
                  ),
                  FittedBox(
                    child: Text(
                      text,
                    ),
                  ),
                ],
              ),
            ),
          );
        },
      ),
    );
  }
}
