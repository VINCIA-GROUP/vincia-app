import 'dart:async';
import 'package:dartz/dartz.dart';
import 'package:mobx/mobx.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';
import 'package:vincia/modules/mock_exam/page/controller/state/question_state.dart';
import 'package:vincia/modules/mock_exam/interfaces/i_mock_exam_service.dart';
import 'package:vincia/shared/model/failure_model.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' as types;

part 'mock_exam_controller.g.dart';

class MockExamController = _MockExamController
    with _$MockExamController;

abstract class _MockExamController with Store {
  final IMockExamService _mockExamService;

  Timer? timeWatcher;

  @observable
  Duration duration = const Duration(seconds: 0);

  @observable
  MockExamQuestionModel? question;

  @observable
  types.User? user;

  @observable
  QuestionState state = InitialState();

  _MockExamController(this._mockExamService);

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
    var sub = await _mockExamService.getUserId();
    user = types.User(id: sub);
    var result = await _mockExamService.getQuestions();
    if (result.isRight()) {
      question = (result as Right).value;
      
      //implementar o banco de dados
    }
    if (result.isLeft()) {
      FailureModel value = (result as Left).value;
      state = FailureState(value);
      return;
    }
    timeWatcher = Timer.periodic(const Duration(seconds: 1), (timer) {
      duration += const Duration(seconds: 1);
    });
  }

  @action
  void answerQuestion(alternativeId) {
    if (state is InitialState && state is! AnsweredQuestionState) {
      timeWatcher?.cancel();
      _mockExamService.sendAnswerQuestion(
          alternativeId, duration, question!.historyOfQuestionId);
      if (alternativeId == question!.answer) {
        state = AnsweredQuestionState(true, alternativeId);
      } else {
        state = AnsweredQuestionState(false, alternativeId);
      }
    }
  }
}
