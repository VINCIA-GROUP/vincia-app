import 'dart:async';
import 'package:dartz/dartz.dart';
import 'package:mobx/mobx.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_answer_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_areas_enum.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_areas_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_cache_model.dart';
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
    final value = duration.toString().split(':');
    return "${value[1]}:${value[2].split('.').first}";
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
  getNextQuestion(int qArea, int qPosition) {
    // question = questions?[qArea][qPosition];
  }

  @action
  void answerQuestion(alternativeId, int qArea, int qPosition) {
    if (state is InitialState && state is! AnsweredQuestionState) {
      timeWatcher?.cancel();
      // final answer = MockExamAnswerModel(alternativeId, duration);
      // _mockExamService.sendAnswerQuestion(
        // question!, answer);
      state = AnsweredQuestionState(alternativeId);
      // questions?[qArea][qPosition].answered = alternativeId;
      // questions?[qArea][qPosition].duration = duration;
    }
  }

  @action
  void submmitExam() {
    _mockExamService.sendMockExamAnswer();
  }
}
