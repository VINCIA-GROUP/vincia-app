import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/essay/page/essay_page.dart';
import '../controllers/essay_theme_controller.dart';
import '../controllers/essay_history_controller.dart';  // Import the EssayHistoryController

class EssayThemePage extends StatefulWidget {
  const EssayThemePage({super.key});

  @override
  State<EssayThemePage> createState() => _EssayThemePageState();
}

class _EssayThemePageState extends State<EssayThemePage> {
  final EssayThemeController _essayThemeController =
      Modular.get<EssayThemeController>();
  final EssayHistoryController _essayHistoryController =
      Modular.get<EssayHistoryController>();  // Get an instance of EssayHistoryController

  var selectedEssayTheme;

  @override
  void initState() {
    super.initState();
    _essayThemeController.fetchEssayTheme();
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
            _essayThemeController.essaytheme = [];
            Modular.to.pop();
          },
        ),
      ),
      body: Observer(
        builder: (_) {
          if (_essayThemeController.essaytheme.isEmpty) {
            return const Center(
              child: CircularProgressIndicator(),
            );
          } else {
            return ListView.builder(
              itemCount: _essayThemeController.essaytheme.length,
              itemBuilder: (context, index) {
                final essaytheme = _essayThemeController.essaytheme[index];
                return _carouselButton(essaytheme.title, essaytheme.tag,
                    () async {
                  final essayData = {
                    // ... add all necessary essay fields here
                    'theme_id': essaytheme.id,
                    // ... other fields
                  };
                  try {
                    final newEssay = await _essayHistoryController.createEssay(essayData);
                    Modular.to.push(MaterialPageRoute(
                      builder: (context) => EssayPage(selectedEssay: newEssay),
                    ));
                  } catch (e) {
                    print('Failed to create essay: $e');
                  }
                });
              },
            );
          }
        },
      ),
    );
  }

  Widget _carouselButton(String title, String tag, Function() onPressed) {
    return Padding(
      padding: const EdgeInsets.all(10.0),
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
              child: Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  SizedBox(
                    height: 100,
                  ),
                  Expanded(
                    child: Text(
                      title,
                      textAlign: TextAlign.center,
                      softWrap: true,
                    ),
                  ),
                  Expanded(
                    child: Text(
                      tag,
                      textAlign: TextAlign.center,
                      softWrap: true,
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
