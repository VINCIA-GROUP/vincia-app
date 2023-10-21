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
          padding: const EdgeInsets.fromLTRB(20, 0, 0, 0),
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
                    essay.totalGrade, essay.isFinished, essay.c1Grade, essay.c2Grade, essay.c3Grade, essay.c4Grade, essay.c5Grade, essay.c1Analysis, essay.c2Analysis, essay.c3Analysis, essay.c4Analysis, essay.c5Analysis, essay.generalAnalysis);
              },
            );
          }
        },
      ),
    );
  }
}

Widget _essayHistoryCard(
    String title, DateTime datetime, double totalGrade, bool isFinished, double c1Grade, double c2Grade, double c3Grade, double c4Grade, double c5Grade, String c1Analysis, String c2Analysis, String c3Analysis, String c4Analysis, String c5Analysis, String generalAnalysis) {
  return Padding(
    padding: const EdgeInsets.all(20.0),
    child: LayoutBuilder(
      builder: (BuildContext context, BoxConstraints constraints) {
        return SizedBox(
          width: constraints.maxWidth,
          child: ElevatedButton(
            style: ElevatedButton.styleFrom(
              backgroundColor:
                  Theme.of(context).colorScheme.primaryContainer,
              foregroundColor:
                  Theme.of(context).colorScheme.onPrimaryContainer,
              shape: const RoundedRectangleBorder(
                borderRadius: BorderRadius.all(Radius.circular(10.0)),
              ),
            ),
            onPressed: () async {
            },
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              mainAxisAlignment: MainAxisAlignment.start,
              children: [
                const SizedBox(
                  height: 20,
                ),
                Row(children: [
                  Text(
                    "Tema: $title",
                    softWrap: true,
                    style: const TextStyle(fontSize: 18.0),
                  ),
                  const Spacer(),
                  Text(
                    DateFormat('dd/MM/yy  HH:mm').format(datetime),
                    softWrap: true,
                    style: const TextStyle(fontSize: 18.0),
                  ),
                ]),
                const SizedBox(
                  height: 30,
                ),
                Text(
                  "Nota geral: $totalGrade",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Comentário geral: $generalAnalysis",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Nota compentência 1: $c1Grade",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Comentários compentência 1: $c1Analysis",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Nota compentência 2: $c2Grade",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Comentários compentência 2: $c2Analysis",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Nota compentência 3: $c3Grade",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Comentários compentência 3: $c3Analysis",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Nota compentência 4: $c4Grade",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Comentários compentência 4: $c4Analysis",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Nota compentência 5: $c5Grade",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
                const SizedBox(
                  height: 10,
                ),
                Text(
                  "Comentários compentência 5: $c5Analysis",
                  textAlign: TextAlign.left,
                  softWrap: true,
                  style: const TextStyle(fontSize: 16.0),
                ),
              ],
            ),
          ),
        );
      },
    ),
  );
}
