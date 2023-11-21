// lib/modules/essay/page/essay_home_page.dart

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/essay/controllers/essay_history_controller.dart';

class EssayHomePage extends StatefulWidget {
  const EssayHomePage({super.key});

  @override
  State<EssayHomePage> createState() => _EssayHomePageState();

}

class _EssayHomePageState extends State<EssayHomePage> {
  final EssayHistoryController _essayHistoryController = Modular.get<EssayHistoryController>();

  @override
  void initState() {
    super.initState();
    _essayHistoryController.fetchUnfinishedEssay();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          padding: EdgeInsets.fromLTRB(20, 0, 0, 0),
          iconSize: 30,
          icon: const Icon(CupertinoIcons.back),
          color: Theme.of(context).colorScheme.onSecondaryContainer,
          onPressed: () {
            Modular.to.pop();
          },
        ),
      ),
      body: SingleChildScrollView(
                child: Padding(
                    padding: const EdgeInsets.fromLTRB(10, 450, 10, 0),
                    child: Column(
                      children: [
                        _carouselButton(" Escolher um tema para nova redação",
                            CupertinoIcons.square_list,
                            () async{
                              Modular.to.pushNamed('/essay/theme');
                            }
                        ),
                            SizedBox(height: 12),
                        _carouselButton(" Iniciar redação com tema aleatório",
                            CupertinoIcons.shuffle, () => null),
                            SizedBox(height: 12),
                        _carouselButton(
                          " Continuar redação",
                          CupertinoIcons.pencil,
                          () async {
                            if( _essayHistoryController.essay.isEmpty) {
                            return Modular.to.pushNamed('/essay/theme');
                          } else {
                            print(_essayHistoryController.essay[0]);
                            return Modular.to.pushNamed('/essay/edit', arguments: _essayHistoryController.essay[0]);
                          }
                          }
                        ),
                        SizedBox(height: 12),
                        _carouselButton(
                          " Histórico de redações",
                          CupertinoIcons.plus_app,
                          () async {
                            Modular.to.pushNamed('/essay/history');
                          }
                        ),
                        SizedBox(height: 12),
                      ],
                    )
                )
            )
    );
  }

  Widget _carouselButton(String text, IconData icon, Function() onPressed) {
    return Padding(
      padding: const EdgeInsets.all(0.0),
      child: LayoutBuilder(
        builder: (BuildContext context, BoxConstraints constraints) {
          return SizedBox(
            width: constraints.maxHeight,
            child: ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Theme.of(context).colorScheme.primaryContainer,
                foregroundColor: Theme.of(context).colorScheme.onPrimaryContainer,
                shape: const RoundedRectangleBorder(
                  borderRadius: BorderRadius.all(Radius.circular(10.0)),
                ),
              ),
              onPressed: onPressed,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  Icon(icon),
                  SizedBox(
                    height: 60,
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
