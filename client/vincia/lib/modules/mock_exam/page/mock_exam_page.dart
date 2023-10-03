import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:flutter_widget_from_html_core/flutter_widget_from_html_core.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_alternative_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_cache_model.dart';
import 'package:vincia/modules/mock_exam/page/controller/mock_exam_controller.dart';
import 'package:vincia/modules/mock_exam/page/controller/state/question_state.dart';
import 'package:vincia/shared/components/error_message_component.dart';

class MockExamPage extends StatefulWidget {
  const MockExamPage({super.key});

  @override
  State<MockExamPage> createState() => _MockExamPageState();
}

class _MockExamPageState extends State<MockExamPage>
    with TickerProviderStateMixin {

  final _mockExamController = Modular.get<MockExamController>();

  late final Future _initQuestion;

  int qPosition = 0;
  int qArea = 0;

  @override
  void initState() {
    super.initState();
    _initQuestion = _mockExamController.init();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: Row(
          children: [
            IconButton(
              iconSize: 32,
              icon: const Icon(Icons.close),
              color: Colors.red,
              onPressed: () {
                Modular.to.pop("/home");
              },
            ),
            IconButton(
              iconSize: 32,
              icon: const Icon(Icons.arrow_back),
              color: Colors.grey,
              onPressed: () {
                if (qArea != 0 && qPosition != 0) {
                  if (qPosition != 0) {
                    qPosition -= 1;
                  } else {
                    qArea -= 1;
                  }
                  _mockExamController.getNextQuestion(qArea, qPosition);
                }
              },
            ),
          ],
        ), 
        title:
          IconButton(
            iconSize: 32,
            icon: const Icon(Icons.menu),
            color: Colors.grey,
            onPressed: () {
              _chooseQuestions(context, _mockExamController.questions);
            },
          ),
        actions: [
          IconButton(
            iconSize: 32,
            icon: const Icon(Icons.arrow_forward),
            color: Colors.grey,
            onPressed: () {
              if (qArea != 3 && qPosition != 45) {
                  if (qPosition != 45) {
                    qPosition += 1;
                  } else {
                    qArea += 1;
                  }
                  _mockExamController.getNextQuestion(qArea, qPosition);
                }
            },
          ),
          IconButton(
            iconSize: 32,
            icon: const Icon(Icons.check),
            color: Colors.green,
            onPressed: () {
              _mockExamController.submmitExam();
            }, 
          )
        ],
      ),
      body: Stack(
        children: [
          Observer(
            builder: (context) {
              var state = _mockExamController.state;
              var question = _mockExamController.question;
              if (state is FailureState) {
                ErrorMessageComponent.showAlertDialog(
                  context,
                  state.failure.errors, 
                  () => {Modular.to.navigate("/home")});
              }
              if (question != null) {
                return ListView(
                  scrollDirection: Axis.vertical,
                  children: [
                    _equestionStatement(
                      context,
                      question.statement),
                    ListView.builder(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount:
                          _mockExamController.question?.alternatives.length,
                      itemBuilder: (BuildContext context, int index) {
                        return _alternatives(
                          context, 
                          index,
                          _mockExamController.question!.alternatives[index]);
                      },
                    ),
                  ],
                );
              }
              return const Center(child: CircularProgressIndicator());
            },
          ),
        ],
      ),
    );
  }

  Widget _equestionStatement(
      BuildContext context, String statement) {
    return Container(
      margin: const EdgeInsets.all(8.0),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.background,
        borderRadius: BorderRadius.circular(8)),
      padding: const EdgeInsets.all(8.0),
      child: HtmlWidget(statement),
    );
  }

  Widget _alternatives(
      BuildContext context, int index, MockExamAlternativeModel alternative) {
    var letter = String.fromCharCode(index + 65);
    var buttonColor = Theme.of(context).colorScheme.primary;
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Observer(builder: (context) {
        return ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: buttonColor,
            foregroundColor: Theme.of(context).colorScheme.onPrimary,
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
            ),
          ),
          onPressed: () {
            _mockExamController.answerQuestion(alternative.id, qArea, qPosition);
          },
          child: Padding(
            padding: const EdgeInsets.symmetric(vertical: 8.0),
            child: Row(
              children: [
                Padding(
                  padding: const EdgeInsets.only(right: 8.0),
                  child: Container(
                    decoration: BoxDecoration(
                      border: Border.all(
                        width: 1,
                        color: Theme.of(context).colorScheme.onPrimary,
                      ),
                      shape: BoxShape.circle,
                    ),
                    child: Padding(
                      padding: const EdgeInsets.all(8.0),
                      child: Text(letter),
                    ),
                  ),
                ),
                Expanded(child: HtmlWidget(alternative.text)),
              ],
            ),
          ),
        );
      }),
    );
  }

  Future _chooseQuestions(BuildContext context, List<List<MockExamCacheModel>>? questionsLists) {
    return showDialog(
      context: context, 
      builder: (BuildContext context) {
        return Dialog(
          child: Container(
            padding: const EdgeInsets.all(16.0),
            width: double.infinity,
            height: double.infinity,
            child: Column (
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  mainAxisAlignment: MainAxisAlignment.end,
                  children: [
                    IconButton(
                      icon: const Icon(Icons.close),
                      onPressed: () {
                        Navigator.of(context).pop();
                      },
                    )
                  ],
                ),
                const Text(
                  'Linguagens, Códigos e suas Tecnologias',
                  style: TextStyle(fontSize: 24.0, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 16.0),
                Expanded(
                  child: GridView.builder(
                    gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                      crossAxisCount: 5
                    ), 
                    itemCount: 45,
                    itemBuilder: (BuildContext context, int index) {
                      return Center(
                        child: Text((index + 1).toString()),
                      );
                    },
                  )
                )
              ],
            ),
          )
        );
      }
    );
  }

  @override
  void dispose() {
    _initQuestion.ignore();
    super.dispose();
  }
}
