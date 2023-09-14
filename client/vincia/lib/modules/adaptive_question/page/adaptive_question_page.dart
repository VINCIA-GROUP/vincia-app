import 'package:flutter/material.dart';
import 'package:flutter_chat_ui/flutter_chat_ui.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:flutter_widget_from_html_core/flutter_widget_from_html_core.dart';
import 'package:vincia/modules/adaptive_question/model/alternative_model.dart';
import 'package:vincia/modules/adaptive_question/page/controller/adaptive_question_controller.dart';
import 'package:vincia/modules/adaptive_question/page/controller/states/question_states.dart';
import 'package:vincia/shared/components/error_message_component.dart';
import 'package:flutter/cupertino.dart';

class AdaptiveQuestionPage extends StatefulWidget {
  const AdaptiveQuestionPage({super.key});

  @override
  State<AdaptiveQuestionPage> createState() => _AdaptiveQuestionPageState();
}

class _AdaptiveQuestionPageState extends State<AdaptiveQuestionPage>
    with TickerProviderStateMixin {
  final _questionController = Modular.get<AdaptiveQuestionController>();

  late final AnimationController _chatButtonAnimationController;
  late final AnimationController _chatAnimationController;
  late final Future _initQuestion;

  @override
  void initState() {
    super.initState();
    _initQuestion = _questionController.init();
    _chatButtonAnimationController = AnimationController(
      duration: const Duration(seconds: 1),
      vsync: this,
    );
    _chatAnimationController = AnimationController(
      duration: const Duration(seconds: 1),
      vsync: this,
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          iconSize: 32,
          icon: const Icon(Icons.close),
          color: Colors.red,
          onPressed: () {
            Modular.to.pop("/home");
          },
        ),
        title: Center(
            child: Container(
                decoration: BoxDecoration(
                    border: Border.all(
                        width: 1,
                        color: Theme.of(context).colorScheme.onBackground),
                    borderRadius: BorderRadius.circular(30)),
                padding:
                    const EdgeInsets.symmetric(vertical: 2.0, horizontal: 8.0),
                child: Observer(builder: (context) {
                  return Text(
                    _questionController.time,
                    style: TextStyle(
                        fontSize: 16,
                        color: Theme.of(context).colorScheme.onBackground),
                  );
                }))),
        actions: [
          IconButton(
            iconSize: 32,
            onPressed: () {
              _questionController.nextQuestion();
            },
            color: Colors.green,
            icon: const Icon(Icons.arrow_forward),
          ),
        ],
      ),
      body: Stack(
        children: [
          Observer(
            builder: (context) {
              var state = _questionController.state;
              var question = _questionController.question;
              if (state is FailureState) {
                ErrorMessageComponent.showAlertDialog(context,
                    state.failure.errors, () => {Modular.to.navigate("/home")});
              }
              if (question != null) {
                return ListView(
                  scrollDirection: Axis.vertical,
                  children: [
                    _equestionStatement(
                        context,
                        question.statement,
                        state is AnsweredQuestionState
                            ? state.isCorrect
                            : null),
                    ListView.builder(
                      shrinkWrap: true,
                      physics: const NeverScrollableScrollPhysics(),
                      itemCount:
                          _questionController.question?.alternatives.length,
                      itemBuilder: (BuildContext context, int index) {
                        return _alternatives(context, index,
                            _questionController.question!.alternatives[index]);
                      },
                    ),
                  ],
                );
              }
              return const Center(child: CircularProgressIndicator());
            },
          ),
          Observer(builder: (context) {
            if (_questionController.state is AnsweredQuestionState) {
              _chatButtonAnimationController.forward();
            }
            if (_questionController.user != null) {
              return Align(
                alignment: Alignment.bottomCenter,
                child: _chat(context),
              );
            }
            return Container();
          }),
        ],
      ),
    );
  }

  Widget _chat(BuildContext context) {
    return SizeTransition(
      sizeFactor: CurvedAnimation(
        parent: _chatButtonAnimationController,
        curve: Curves.fastOutSlowIn,
      ),
      axis: Axis.vertical,
      axisAlignment: -1,
      child: SizedBox(
        width: double.infinity,
        child: GestureDetector(
          onVerticalDragEnd: (details) {
            _questionController.chatOpen();
            if (_chatAnimationController.isCompleted) {
              _chatAnimationController.reverse();
            } else {
              _chatAnimationController.forward();
            }
          },
          child: LayoutBuilder(builder: (context, constraints) {
            return Column(
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Container(
                  decoration: BoxDecoration(
                      borderRadius: const BorderRadius.only(
                        topLeft: Radius.circular(20.0),
                        topRight: Radius.circular(20.0),
                      ),
                      boxShadow: [
                        BoxShadow(
                            color: Theme.of(context)
                                .colorScheme
                                .secondary
                                .withOpacity(0.5),
                            spreadRadius: 5,
                            blurRadius: 15),
                      ]),
                  child: Observer(builder: (context) {
                    return Icon(
                      _questionController.chatIsOpen!
                          ? CupertinoIcons.chevron_down
                          : CupertinoIcons.chevron_up,
                      color: Theme.of(context).colorScheme.onSecondary,
                      size: 30,
                      fill: 0.9,
                    );
                  }),
                ),
                Container(
                  decoration: BoxDecoration(
                    color: Theme.of(context).colorScheme.secondary,
                    borderRadius: const BorderRadius.only(
                      topLeft: Radius.circular(20.0),
                      topRight: Radius.circular(20.0),
                    ),
                  ),
                  height: 40,
                  alignment: Alignment.center,
                  child: Text(
                    "CHAT",
                    style: TextStyle(
                        color: Theme.of(context).colorScheme.onSecondary),
                  ),
                ),
                SizeTransition(
                  sizeFactor: CurvedAnimation(
                    parent: _chatAnimationController,
                    curve: Curves.fastOutSlowIn,
                  ),
                  axis: Axis.vertical,
                  axisAlignment: -1,
                  child: Container(
                      height: constraints.maxHeight - 40 - 30,
                      color: Theme.of(context).colorScheme.secondary,
                      child: Observer(
                        builder: (context) {
                          return Chat(
                              theme: DefaultChatTheme(
                                backgroundColor:
                                    Theme.of(context).colorScheme.secondary,
                                inputBackgroundColor: Theme.of(context)
                                    .colorScheme
                                    .secondaryContainer,
                                inputTextColor: Theme.of(context)
                                    .colorScheme
                                    .onSecondaryContainer,
                              ),
                              messages: _questionController.messages,
                              onSendPressed:
                                  _questionController.handleSendPressed,
                              showUserNames: true,
                              user: _questionController.user!);
                        },
                      )),
                ),
              ],
            );
          }),
        ),
      ),
    );
  }

  Widget _equestionStatement(
      BuildContext context, String statement, bool? isCorrect) {
    return Container(
      margin: const EdgeInsets.all(8.0),
      decoration: BoxDecoration(
        color: Theme.of(context).colorScheme.background,
        borderRadius: BorderRadius.circular(8),
        boxShadow: [
          BoxShadow(
            color: isCorrect == null
                ? Theme.of(context).colorScheme.outline.withOpacity(0.5)
                : isCorrect
                    ? Colors.green.withOpacity(0.5)
                    : Colors.red.withOpacity(0.5),
            spreadRadius: 5,
            blurRadius: 5,
          ),
        ],
      ),
      padding: const EdgeInsets.all(8.0),
      child: HtmlWidget(statement),
    );
  }

  Widget _alternatives(
      BuildContext context, int index, AlternativeModel alternative) {
    var letter = String.fromCharCode(index + 65);
    var buttonColor = Theme.of(context).colorScheme.primary;
    var borderColor = Theme.of(context).colorScheme.primary;
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Observer(builder: (context) {
        if (_questionController.state is AnsweredQuestionState) {
          var state = _questionController.state as AnsweredQuestionState;
          borderColor = alternative.id == _questionController.question!.answer
              ? Colors.green
              : Theme.of(context).colorScheme.primary;
          if (state.alternativeId == alternative.id) {
            buttonColor = state.isCorrect ? Colors.green : Colors.red;
            borderColor = buttonColor;
          }
        }
        return ElevatedButton(
          style: ElevatedButton.styleFrom(
            backgroundColor: buttonColor,
            foregroundColor: Theme.of(context).colorScheme.onPrimary,
            shape: RoundedRectangleBorder(
              borderRadius: const BorderRadius.all(Radius.circular(10.0)),
              side: BorderSide(
                  color: borderColor, width: 3.0), // <--- borda verde aqui
            ),
          ),
          onPressed: () => _questionController.answerQuestion(alternative.id),
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
    _chatButtonAnimationController.dispose();
    _chatAnimationController.dispose();
    super.dispose();
  }
}
