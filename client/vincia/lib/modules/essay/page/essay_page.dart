import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/essay/services/essay_service.dart';

class EssayPage extends StatefulWidget {
  const EssayPage({super.key});

  @override
  _EssayPageState createState() => _EssayPageState();
}

class _EssayPageState extends State<EssayPage> {
  static const String apiUrl = String.fromEnvironment("API_URL");
  late final ImagePickerHandler _imagePickerHandler;

  _EssayPageState() : _imagePickerHandler = ImagePickerHandler(apiUrl);

  String _transcription = '';

  void _updateTranscription(String transcription) {
    setState(() {
      _transcription = transcription;
    });
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
        actions: <Widget>[
          IconButton(
            padding: EdgeInsets.fromLTRB(0, 0, 20, 0),
            iconSize: 32,
            icon: const Icon(CupertinoIcons.square_arrow_down),
            color: Theme.of(context).colorScheme.onSecondaryContainer,
            onPressed: () {
              Modular.to.pop();
            },
          )
        ],
      ),
      body: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(10, 0, 10, 0),
          child: Column(
            children: [
              Container(
                height: MediaQuery.of(context).size.height * 0.08,
                width: MediaQuery.of(context).size.width * 1,
                decoration: BoxDecoration(
                  color: Theme.of(context).colorScheme.primaryContainer,
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Center(
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(
                        'Tema',
                        style: TextStyle(color: Theme.of(context).colorScheme.onPrimaryContainer, fontWeight: FontWeight.bold),
                      ),
                      Text(
                        'Tema tema tema tema tema tema tema tema tema',
                        style: TextStyle(color: Theme.of(context).colorScheme.onPrimaryContainer),
                      ),
                    ],
                  ),
                ),
              ),
              Container(
                height: 450,
                margin: EdgeInsets.fromLTRB(0, 15, 0, 15),
                padding: const EdgeInsets.symmetric(horizontal: 10),
                decoration: BoxDecoration(
                  color: Colors.white,
                  borderRadius: BorderRadius.circular(12),
                  boxShadow: [
                    BoxShadow(
                      color: Colors.grey,
                      blurRadius: 4,
                      offset: Offset(2, 2), // Shadow position
                    ),
                  ],
                ),
                child: TextField(
                  maxLines: null,
                  style: TextStyle(
                    color: Colors.black,
                  ),
                  decoration: InputDecoration(
                    hintText: 'Insira sua redação',
                    hintStyle: TextStyle(
                      color: Colors.black,
                    ),
                    border: InputBorder.none,
                  ),
                  controller: TextEditingController(text: _transcription),
                ),
              ),
              Column(
                children: [
                  _carouselButton(
                    " Acessar texto motivadores",
                    CupertinoIcons.today,
                    () => null
                  ),
                  _carouselButton(
                    " Digitalizar redação",
                    CupertinoIcons.doc_text_viewfinder,
                    () async {
                      final transcription = await _imagePickerHandler.pickImage(context);
                      if (transcription != null) {
                        _updateTranscription(transcription);
                      }
                    },
                  ),
                  _carouselButton(
                    " Enviar para correção",
                    CupertinoIcons.chart_bar,
                    () => null
                  ),
                ],
              )
            ],
          ),
        ),
      ),
    );
  }

  Widget _carouselButton(String text, IconData icon, Function() onPressed) {
    return Padding(
      padding: const EdgeInsets.all(5.0),
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
                  const SizedBox(
                    height: 50,
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
