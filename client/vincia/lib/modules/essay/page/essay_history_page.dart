import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import '../controllers/essay_history_controller.dart';
import 'package:intl/intl.dart';

class EssayHistoryPage extends StatefulWidget {
  const EssayHistoryPage({super.key});

  @override
  State<EssayHistoryPage> createState() => _EssayHistoryPageState();
}

class _EssayHistoryPageState extends State<EssayHistoryPage> {
  final EssayHistoryController _essayHistoryController =
      Modular.get<EssayHistoryController>();

  @override
  void initState() {
    super.initState();
    _essayHistoryController.fetchEssayHistory();
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
            _essayHistoryController.essay = [];
            Modular.to.pop();
          },
        ),
      ),
      body: Observer(
        builder: (_) {
          if (_essayHistoryController.essay.isEmpty) {
            return const Center(
              child: CircularProgressIndicator(),
            );
          } else {
            return ListView.builder(
              itemCount: _essayHistoryController.essay.length,
              itemBuilder: (context, index) {
                final essay = _essayHistoryController.essay[index];

                return _essayHistoryCard(essay.title, essay.createdAt,
                    essay.totalGrade, essay.isFinished);
              },
            );
          }
        },
      ),
    );
  }
}

Widget _essayHistoryCard(
    String title, DateTime datetime, double totalGrade, bool isFinished) {
  return Padding(
    padding: const EdgeInsets.all(10.0),
    child: LayoutBuilder(
      builder: (BuildContext context, BoxConstraints constraints) {
        return SizedBox(
          width: constraints
              .maxWidth,
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor: Theme.of(context).colorScheme.primaryContainer,
              foregroundColor: Theme.of(context).colorScheme.onPrimaryContainer,
              shape: const RoundedRectangleBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
              ),
            ),
            onPressed: () async {
              //Modular.to.pushNamed('/essay/history', arguments: title);
            },
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(
                  height:
                      10,
                ),
                Text( 
                  "Título da redação: $title",
                  textAlign: TextAlign.center,
                  softWrap: true,
                ),
                Row(
                  mainAxisAlignment: MainAxisAlignment
                      .spaceBetween, 
                  children: [
                    SizedBox(
                      height: 30,
                    ),
                    Text(
                      totalGrade.toString(),
                      //textAlign: TextAlign.left,
                      softWrap: true,
                    ),
                    SizedBox(
                      height: 10,
                    ),
                    Text(
                      DateFormat('dd/MM/yy  HH:mm').format(datetime),
                      textAlign: TextAlign.right,
                      softWrap: true,
                    ),
                  ],
                )
              ],
            ),
          ),
        );
      },
    ),
  );
}
