import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:flutter_widget_from_html_core/flutter_widget_from_html_core.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_alternative_model.dart';
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

  @override
  void initState() {
    super.initState();
    _initQuestion = _mockExamController.init();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: PreferredSize(
        preferredSize: const Size.fromHeight(kToolbarHeight),
        child: AppBar(
          automaticallyImplyLeading: false,
          actions: <Widget>[
            Expanded(
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
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
                    color: Theme.of(context).colorScheme.primary,
                    onPressed: () {
                      if (_mockExamController.questionIndex != 0) {
                        _mockExamController.questionIndex -= 1;
                        _mockExamController.getNextQuestion(_mockExamController.questionIndex);
                      }
                    },
                  ),
                  IconButton(
                    iconSize: 32,
                    icon: const Icon(Icons.menu),
                    color: Theme.of(context).colorScheme.primary,
                    onPressed: () {
                      _chooseQuestions(context);
                    },
                  ),
                  IconButton(
                    iconSize: 32,
                    icon: const Icon(Icons.arrow_forward),
                    color: Theme.of(context).colorScheme.primary,
                    onPressed: () {
                      if (_mockExamController.questionIndex != 179) {
                        _mockExamController.questionIndex += 1;
                        _mockExamController.getNextQuestion(_mockExamController.questionIndex);
                      }
                    },
                  ),
                  IconButton(
                    iconSize: 32,
                    icon: const Icon(Icons.check),
                    color: Colors.green,
                    onPressed: () {
                      _mockExamController.submmitExam();
                      Modular.to.pop("/home");
                    }, 
                  )
                ],
              )
            )
          ],
        ),
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
                    Container(
                      margin: const EdgeInsets.only(left: 16.0),
                      decoration: BoxDecoration(
                      color: Theme.of(context).colorScheme.background,
                      borderRadius: BorderRadius.circular(8)),
                      child: Text(
                        (_mockExamController.questionIndex + 1).toString(), 
                        style: TextStyle(
                          color: Theme.of(context).colorScheme.primary,
                          fontWeight: FontWeight.bold
                        ),
                      ),
                    ),
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
        if (_mockExamController.state is AnsweredQuestionState) {
          var state = _mockExamController.state as AnsweredQuestionState;
          if (state.alternativeId == alternative.id) {
            buttonColor = Theme.of(context).colorScheme.secondary;
          }
        }
        return ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: buttonColor,
            foregroundColor: Theme.of(context).colorScheme.onPrimary,
            shape: const RoundedRectangleBorder(
              borderRadius: BorderRadius.all(Radius.circular(10.0)),
            ),
          ),
          onPressed: () {
            _mockExamController.answerQuestion(alternative.id, _mockExamController.questionIndex);
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

  Future _chooseQuestions(BuildContext context) {
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
                Expanded(
                  child: SingleChildScrollView(
                    child: Column(
                      children: [
                        const Text(
                          'Linguagens, Códigos e suas Tecnologias',
                          style: TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 10.0),
                        GridView.builder(
                          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                            crossAxisCount: 4,
                          ),
                          shrinkWrap: true,
                          physics: const NeverScrollableScrollPhysics(),
                          itemCount: 45,
                          itemBuilder: (context, index) {
                            return Padding(
                              padding: const EdgeInsets.all(6.0),
                              child: TextButton(
                                onPressed: () async {
                                  if (index != _mockExamController.questionIndex) {
                                    await _mockExamController.getNextQuestion(index);
                                    _mockExamController.questionIndex = index;
                                  }
                                },
                                style: ButtonStyle(
                                  backgroundColor: _mockExamController.answers![index] != "" 
                                    ? null
                                    : MaterialStateProperty.all<Color>(Theme.of(context).colorScheme.primary),
                                ),
                                child: Text(
                                  (index + 1).toString(),
                                  style: _mockExamController.answers![index] != ""
                                  ? TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.primary)
                                  : TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.background),
                                ),
                              ),
                            );
                          },  
                        ),
                        const Text(
                          'Ciências Humanas e suas Tecnologias',
                          style: TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 10.0),
                        GridView.builder(
                          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                            crossAxisCount: 4,
                          ),
                          shrinkWrap: true,
                          physics: const NeverScrollableScrollPhysics(),
                          itemCount: 45,
                          itemBuilder: (context, index) {
                            return Padding(
                              padding: const EdgeInsets.all(6.0),
                              child: TextButton(
                                onPressed: () async {
                                  if (index != _mockExamController.questionIndex + 45) {
                                    await _mockExamController.getNextQuestion(index + 45);
                                    _mockExamController.questionIndex = index + 45;
                                  }
                                },
                                style: ButtonStyle(
                                  backgroundColor: _mockExamController.answers![index + 45] != "" 
                                    ? null
                                    : MaterialStateProperty.all<Color>(Theme.of(context).colorScheme.primary),
                                ),
                                child: Text(
                                  (index + 46).toString(),
                                  style: _mockExamController.answers![index + 45] != ""
                                  ? TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.primary)
                                  : TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.background),
                                ),
                              ),
                            );
                          },  
                        ),
                        const Text(
                          'Ciências da Natureza e suas Tecnologias',
                          style: TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 10.0),
                        GridView.builder(
                          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                            crossAxisCount: 4,
                          ),
                          shrinkWrap: true,
                          physics: const NeverScrollableScrollPhysics(),
                          itemCount: 45,
                          itemBuilder: (context, index) {
                            return Padding(
                              padding: const EdgeInsets.all(6.0),
                              child: TextButton(
                                onPressed: () async {
                                  if (index != _mockExamController.questionIndex + 90) {
                                    await _mockExamController.getNextQuestion(index + 90);
                                    _mockExamController.questionIndex = index + 90;
                                  }
                                },
                                style: ButtonStyle(
                                  backgroundColor: _mockExamController.answers![index + 90] != "" 
                                    ? null
                                    : MaterialStateProperty.all<Color>(Theme.of(context).colorScheme.primary),
                                ),
                                child: Text(
                                  (index + 91).toString(),
                                  style: _mockExamController.answers![index + 90] != ""
                                  ? TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.primary)
                                  : TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.background),
                                ),
                              ),
                            );
                          },  
                        ),
                        const Text(
                          'Matemática e suas Tecnologias',
                          style: TextStyle(fontSize: 18.0, fontWeight: FontWeight.bold),
                        ),
                        const SizedBox(height: 10.0),
                        GridView.builder(
                          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                            crossAxisCount: 4,
                          ),
                          shrinkWrap: true,
                          physics: const NeverScrollableScrollPhysics(),
                          itemCount: 45,
                          itemBuilder: (context, index) {
                            return Padding(
                              padding: const EdgeInsets.all(6.0),
                              child: TextButton(
                                onPressed: () async {
                                  if (index != _mockExamController.questionIndex) {
                                    await _mockExamController.getNextQuestion(index + 135);
                                    _mockExamController.questionIndex = index + 135;
                                  }
                                },
                                style: ButtonStyle(
                                  backgroundColor: _mockExamController.answers![index + 135] != "" 
                                    ? null
                                    : MaterialStateProperty.all<Color>(Theme.of(context).colorScheme.primary),
                                ),
                                child: Text(
                                  (index + 136).toString(),
                                  style: _mockExamController.answers![index + 135] != ""
                                  ? TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.primary)
                                  : TextStyle(fontSize: 14.0, color: Theme.of(context).colorScheme.background),
                                ),
                              ),
                            );
                          },  
                        ),
                      ]
                    ),
                  )
                )
              ],
            )
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
