import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:vincia/modules/essay/services/essay_service.dart';
import 'package:vincia/modules/essay/models/essay_model.dart';
import 'package:auth0_flutter/auth0_flutter.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

const apiUrl = String.fromEnvironment("API_URL");  // Replace with your backend API URL

class EssayAnalysisService {
  final String apiUrl;
  final http.Client client;

  EssayAnalysisService(this.apiUrl, this.client);

  Future<Map<String, dynamic>> analyzeEssay(Map<String, dynamic> essayData) async {
    final response = await client.post(
      Uri.parse('$apiUrl/api/essay/analysis'),
      headers: {
        'Content-Type': 'application/json',
      },
      body: jsonEncode(essayData),
    );

    if (response.statusCode == 200) {
      return jsonDecode(response.body);
    } else {
      throw Exception('Failed to analyze essay: ${response.reasonPhrase}');
    }
  }
}

class EssayPage extends StatefulWidget {
  final Essay selectedEssay;
  final Auth0 auth;
  final http.Client client;

  const EssayPage({
    required this.selectedEssay,
    required this.auth,
    required this.client,
    Key? key,
  }) : super(key: key);

  @override
  _EssayPageState createState() => _EssayPageState();
}

class _EssayPageState extends State<EssayPage> {
  late final ImagePickerHandler _imagePickerHandler;
  String _transcription = '';

  @override
  void initState() {
    super.initState();
    final TranscriptionService transcriptionService = TranscriptionService(widget.auth, widget.client);
    _imagePickerHandler = ImagePickerHandler(transcriptionService);
    if (widget.selectedEssay.content != null) {
      _transcription = widget.selectedEssay.content!;
    }
  }

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
                        style: TextStyle(
                          color: Theme.of(context).colorScheme.onPrimaryContainer,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      Padding(
                        padding: const EdgeInsets.symmetric(horizontal: 16.0),
                        child: Text(
                          widget.selectedEssay.title,
                          style: TextStyle(
                            color: Theme.of(context).colorScheme.onPrimaryContainer,
                          ),
                        ),
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
                  boxShadow: const [
                    BoxShadow(
                      color: Colors.grey,
                      blurRadius: 4,
                      offset: Offset(2, 2),
                    ),
                  ],
                ),
                child: TextField(
                  maxLines: null,
                  style: const TextStyle(
                    color: Colors.black,
                  ),
                  decoration: const InputDecoration(
                    hintText: 'Insira sua redação',
                    hintStyle: TextStyle(
                      color: Colors.black,
                    ),
                    border: InputBorder.none,
                  ),
                  onChanged: (value) => _updateTranscription(value),
                ),
              ),
              Column(
                children: [
                  _carouselButton(
                    " Acessar texto motivadores",
                    CupertinoIcons.today,
                    () => null,
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
                    () async {
                      final essayData = {
                        'id': widget.selectedEssay.essayId,
                        'theme_id': widget.selectedEssay.themeId,
                        'theme_title': widget.selectedEssay.title,
                        'essay_title': widget.selectedEssay.title,
                        'essay_content': _transcription,
                      };

                      final analysisService = EssayAnalysisService(apiUrl, http.Client());
                      try {
                        final analysis = await analysisService.analyzeEssay(essayData);
                        // Handle analysis result, e.g., show it to the user
                      } catch (e) {
                        print('Failed to analyze essay: $e');
                        // Optionally, display an error message to the user
                      }
                    },
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
