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
              icon: const Icon(Icons.menu),
              color: Colors.grey,
              onPressed: () {
                //
              },
            ),
          ],
        ), 
        title: Center(
          child: Container(
            decoration: BoxDecoration(
              border: Border.all(
                width: 1,
                color: Theme.of(context).colorScheme.onBackground),
              borderRadius: BorderRadius.circular(30)),
            padding: const EdgeInsets.symmetric(
              vertical: 2.0, 
              horizontal: 8.0),
            child: Observer(builder: (context) {
              return Text(
                _mockExamController.time,
                style: TextStyle(
                  fontSize: 16,
                  color: Theme.of(context).colorScheme.onBackground),
              );
            })
          )
        ),
        actions: [
          IconButton(
            iconSize: 32,
            onPressed: () {
              //
            },
            color: Colors.grey,
            icon: const Icon(Icons.arrow_back),
          ),
          IconButton(
            iconSize: 32,
            onPressed: () {
              //
            }, 
            color: Colors.grey,
            icon: const Icon(Icons.arrow_forward),
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
          onPressed: () => _mockExamController.answerQuestion(alternative.id),
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

  @override
  void dispose() {
    _initQuestion.ignore();
    super.dispose();
  }
}
