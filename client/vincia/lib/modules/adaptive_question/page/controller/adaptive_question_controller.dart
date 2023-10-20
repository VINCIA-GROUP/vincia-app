import 'dart:async';
import 'package:dartz/dartz.dart';
import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';
import 'package:mobx/mobx.dart';
import 'package:uuid/uuid.dart';
import 'package:vincia/modules/adaptive_question/interfaces/i_adaptive_question_service.dart';
import 'package:vincia/modules/adaptive_question/model/adaptive_question_model.dart';
import 'package:vincia/modules/adaptive_question/page/controller/states/question_states.dart';
import 'package:vincia/shared/model/failure_model.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' as types;

part 'adaptive_question_controller.g.dart';

// ignore: library_private_types_in_public_api
class AdaptiveQuestionController = _AdaptiveQuestionController
    with _$AdaptiveQuestionController;

abstract class _AdaptiveQuestionController with Store {
  final IAdaptiveQuestionService _questionService;

  final _chatBotUser = const types.User(
    id: '82091009-a484-4a89-ae75-a22bf8d6f3ac',
  );

  Future<Either<FailureModel, String>>? _historyOfQuestionId;

  Timer? timeWatcher;

  @observable
  Duration duration = const Duration(seconds: 0);

  @observable
  AdaptiveQuestionModel? question;

  @observable
  bool? chatIsOpen = false;

  @observable
  List<types.Message> messages = [];

  @observable
  types.User? user;

  @observable
  QuestionState state = InitialState();

  _AdaptiveQuestionController(this._questionService);

  @computed
  String get time {
    final value = duration.toString().split(':');
    return "${value[1]}:${value[2].split('.').first}";
  }

  @action
  Future<void> init() async {
    state = InitialState();
    question = null;
    duration = const Duration(seconds: 0);
    timeWatcher?.cancel();
    var sub = await _questionService.getUserId();
    user = types.User(id: sub);
    var result = await _questionService.getQuestion();
    if (result.isRight()) {
      question = (result as Right).value;
    }
    if (result.isLeft()) {
      FailureModel value = (result as Left).value;
      state = FailureState(value);
      return;
    }
    timeWatcher = Timer.periodic(const Duration(seconds: 1), (timer) {
      duration += const Duration(seconds: 1);
    });

    final textMessage = types.TextMessage(
      author: _chatBotUser,
      createdAt: DateTime.now().millisecondsSinceEpoch,
      id: const Uuid().v4(),
      text:
          "Olá, sou o Vincia Bot é irei esclarecer todas as suas dúvidas. Como posso te ajudar?",
    );
    messages.add(textMessage);
  }

  @action
  Future<void> answerQuestion(alternativeId) async {
    if (state is InitialState && state is! AnsweredQuestionState) {
      timeWatcher?.cancel();
      if (alternativeId == question!.answer) {
        state = AnsweredQuestionState(true, alternativeId);
      } else {
        state = AnsweredQuestionState(false, alternativeId);
      }
      _historyOfQuestionId = _questionService.sendAnswerQuestion(
          alternativeId, duration, question!.id);
    }
  }

  @action
  void chatOpen() {
    chatIsOpen = chatIsOpen == false;
  }

  @action
  Future<void> nextQuestion() async {
    question = null;
    await _historyOfQuestionId;
    Modular.to.popAndPushNamed('/question');
  }

  @action
  Future<void> handleSendPressed(types.PartialText message) async {
    var historyOfQuestion = await _historyOfQuestionId;
    if (historyOfQuestion == null || historyOfQuestion.isLeft()) {
      FailureModel value = (historyOfQuestion as Left).value;
      state = FailureState(value);
      return;
    }
    var hId = (historyOfQuestion as Right).value;
    final textMessage = types.TextMessage(
      author: user!,
      createdAt: DateTime.now().millisecondsSinceEpoch,
      id: const Uuid().v4(),
      text: message.text,
    );
    messages = List.from(messages..insert(0, textMessage));
    var result = await _questionService.sendMessage(message.text, hId);
    if (result.isRight()) {
      var response = (result as Right).value;
      final textMessage = types.TextMessage(
        author: _chatBotUser,
        createdAt: DateTime.now().millisecondsSinceEpoch,
        id: const Uuid().v4(),
        text: response,
      );
      messages = List.from(messages..insert(0, textMessage));
    }
    if (result.isLeft()) {
      FailureModel value = (result as Left).value;
      state = FailureState(value);
    }
  }
}
