import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import '../controllers/essay_theme_controller.dart';


class EssayThemePage extends StatefulWidget {
  const EssayThemePage({super.key});

  @override
  State<EssayThemePage> createState() => _EssayThemePageState();
}

class _EssayThemePageState extends State<EssayThemePage> {
  final EssayThemeController _essayThemeController = Modular.get<EssayThemeController>();

  @override
  void initState() {
    super.initState();
    _essayThemeController.fetchEssayTheme();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Essay Theme'),
      ),
      body: Observer(
        builder: (_) {
          if( _essayThemeController.essaytheme.isEmpty) {
            return const Center(child: CircularProgressIndicator(),);
          } else {
            return ListView.builder(
              itemCount: _essayThemeController.essaytheme.length,
              itemBuilder: (context, index) {
                final essay = _essayThemeController.essaytheme[index];

                return ListTile(
                  title: Text(essay.title),
                  subtitle: Text(essay.tag.toString()),
                );
              },
            );
          }
        },
      ),
    );
  }
}
