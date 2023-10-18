import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/home/page/controller/home_controller.dart';

class HomePage extends StatelessWidget {
  final HomeController _homeController = Modular.get<HomeController>();

  final itens = [
    "Coordenadas cartesianas: Entender como as coordenadas cartesianas funcionam e como elas podem ser usadas para descrever pontos em um plano.",
    "Distância e inclinação: Aprender como encontrar a distância entre dois pontos e a inclinação de uma reta usando coordenadas cartesianas."
  ];

  HomePage({super.key}) {
    _homeController.init();
    _homeController.getRating();
  }

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
                child: Padding(
                  padding: const EdgeInsets.all(4.0),
                  child: Observer(builder: (context) {
                    return Text(_homeController.rating.toString());
                  }),
                ),
              ),
            ),
            PopupMenuButton(
              icon: Row(
                children: [
                  Observer(builder: (context) {
                    var pictureUrl = _homeController.user?.pictureUrl;
                    if (pictureUrl != null) {
                      return CircleAvatar(
                        backgroundImage: NetworkImage(pictureUrl.toString()),
                      );
                    } else {
                      return const CircleAvatar(
                        backgroundImage:
                            AssetImage("assets/images/avatar_default.png"),
                      );
                    }
                  }),
                  const Icon(Icons.arrow_drop_down_sharp)
                ],
              ),
              itemBuilder: (BuildContext context) {
                return const <PopupMenuEntry>[
                  PopupMenuItem(
                    value: "profile",
                    child: Text('Perfil'),
                  ),
                  PopupMenuItem(
                    value: "logout",
                    child: Text('Log out'),
                  ),
                ];
              },
              onSelected: (value) {
                _homeController.menuFunction(value);
              },
            ),
          ],
        ),
        body: Column(
          children: [
            Expanded(
              child: SingleChildScrollView(
                child: Padding(
                  padding: const EdgeInsets.all(16.0),
                  child: Container(
                    padding: const EdgeInsets.all(8.0),
                    width: double.infinity,
                    decoration: BoxDecoration(
                      border: Border.all(
                          color: Theme.of(context).colorScheme.primary),
                      borderRadius: BorderRadius.circular(5),
                    ),
                    child: Column(children: [
                      Padding(
                        padding: const EdgeInsets.only(bottom: 8),
                        child: Text(
                          "Guia de estudos",
                          style: TextStyle(
                              fontWeight: FontWeight.bold,
                              fontSize: 16,
                              color: Theme.of(context).colorScheme.primary),
                        ),
                      ),
                      // const Text("...")
                      ListView.builder(
                        shrinkWrap: true,
                        itemCount: itens.length,
                        itemBuilder: (context, index) {
                          return Padding(
                            padding: const EdgeInsets.only(bottom: 8),
                            child: Row(
                              children: [
                                Checkbox(
                                  value: false,
                                  onChanged: (bool? newValue) {},
                                ),
                                Expanded(child: Text(itens[index])),
                              ],
                            ),
                          );
                        },
                      )
                    ]),
                  ),
                ),
              ),
            ),
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
                        Modular.to.pushNamed("/question");
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
                      () {
                        Modular.to.pushNamed("/essay");
                      },
                    ),
                    _carouselButton(
                      "Estatisticas",
                      Icons.stacked_bar_chart_outlined,
                      () {},
                    ),
                    _carouselButton(
                      "Atualizar",
                      Icons.update,
                      () async {
                        Modular.to.navigate("/");
                      },
                    ),
                    _carouselButton(
                      "Log out",
                      Icons.logout,
                      () async {
                        var auth = Modular.get<Auth0>();
                        const scheme =
                            String.fromEnvironment("AUTH0_CUSTOM_SCHEME");
                        await auth.webAuthentication(scheme: scheme).logout();
                        Modular.to.navigate("/");
                      },
                    )
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
