import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import '../controllers/essay_history_controller.dart';


class EssayHistoryPage extends StatefulWidget {
  const EssayHistoryPage({super.key});

  @override
  State<EssayHistoryPage> createState() => _EssayHistoryPageState();
}

class _EssayHistoryPageState extends State<EssayHistoryPage> {
  final EssayHistoryController _essayHistoryController = Modular.get<EssayHistoryController>();

  @override
  void initState() {
    super.initState();
    _essayHistoryController.fetchEssayHistory();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Essay History'),
      ),
      body: Observer(
        builder: (_) {
          if( _essayHistoryController.essay.isEmpty) {
            return const Center(child: CircularProgressIndicator(),);
          } else {
            return ListView.builder(
              itemCount: _essayHistoryController.essay.length,
              itemBuilder: (context, index) {
                final essay = _essayHistoryController.essay[index];

                return ListTile(
                  title: Text(essay.title),
                  subtitle: Text(essay.createdAt.toString()),
                );
              },
            );
          }
        },
      ),
    );
  }
}
