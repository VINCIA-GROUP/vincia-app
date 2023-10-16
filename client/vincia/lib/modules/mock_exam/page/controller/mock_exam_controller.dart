import 'dart:async';
import 'package:dartz/dartz.dart';
import 'package:mobx/mobx.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_answer_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';
import 'package:vincia/modules/mock_exam/page/controller/state/question_state.dart';
import 'package:vincia/modules/mock_exam/interfaces/i_mock_exam_service.dart';
import 'package:vincia/modules/mock_exam/services/mock_exam_cache.dart';
import 'package:vincia/shared/model/failure_model.dart';
import 'package:flutter_chat_types/flutter_chat_types.dart' as types;

part 'mock_exam_controller.g.dart';

// ignore: library_private_types_in_public_api
class MockExamController = _MockExamController
    with _$MockExamController;

abstract class _MockExamController with Store {
  final IMockExamService _mockExamService;

  Timer? timeWatcher;

  final cache = MockExamCache.instance;

  @observable
  Duration duration = const Duration(seconds: 0);

  @observable
  types.User? user;

  @observable
  List<String>? questions;

  @observable
  List<String>? answers;
  
  @observable
  List<String>? durations;
  
  @observable
  MockExamQuestionModel? question;

  @observable
  QuestionState state = InitialState();

  _MockExamController(this._mockExamService);

  @computed
  String get time {
    return duration.inSeconds.toString();
  }

  @action
  Future<void> init() async {
    state = InitialState();
    duration = const Duration(seconds: 0);
    timeWatcher?.cancel();
    var sub = await _mockExamService.getUserId();
    user = types.User(id: sub);
    
    var result = await _mockExamService.getQuestions();
    if (result.isRight()) {
      questions = (result as Right).value.questions;
      answers = (result as Right).value.answers;
      durations = (result as Right).value.durations;
      var questionData = await _mockExamService.getQuestion(questions![0]);
      if (questionData.isRight()) {
        question = (questionData as Right).value;
      }
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
  Future<void> getNextQuestion(int questionIndex) async {
    durations![questionIndex] = calculateDuration(questionIndex);

    state = InitialState();
    duration = const Duration(seconds: 0);
    timeWatcher?.cancel();
    question = null;

    String questionId = questions![questionIndex];
    var questionData = await _mockExamService.getQuestion(questionId);
    if (questionData.isRight()) {
      question = (questionData as Right).value;
    } 
    if (questionData.isLeft()) {
      FailureModel value = (questionData as Left).value;
      state = FailureState(value);
      return;
    }
    timeWatcher = Timer.periodic(const Duration(seconds: 1), (timer) {
      duration += const Duration(seconds: 1);
    });
  }

  @action
  Future<void> answerQuestion(String alternativeId, int questionIndex) async {
    state = AnsweredQuestionState(alternativeId);
    answers![questionIndex] = alternativeId;
    durations![questionIndex] = calculateDuration(questionIndex);
    final answer = MockExamAnswerModel(answers!, durations!);
    await _mockExamService.sendQuestionAnswer(answer);
}

  @action
  void submmitExam() {
    _mockExamService.submmitMockExam();
  }

  String calculateDuration(int questionIndex) {
    return (int.parse(durations![questionIndex]) + int.parse(time)).toString();
  }
}
