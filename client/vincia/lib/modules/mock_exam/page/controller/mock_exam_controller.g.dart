// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'mock_exam_controller.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic, no_leading_underscores_for_local_identifiers

mixin _$MockExamController on _MockExamController, Store {
  Computed<String>? _$timeComputed;

  @override
  String get time => (_$timeComputed ??=
          Computed<String>(() => super.time, name: '_MockExamController.time'))
      .value;

  late final _$durationAtom =
      Atom(name: '_MockExamController.duration', context: context);

  @override
  Duration get duration {
    _$durationAtom.reportRead();
    return super.duration;
  }

  @override
  set duration(Duration value) {
    _$durationAtom.reportWrite(value, super.duration, () {
      super.duration = value;
    });
  }

  late final _$userAtom =
      Atom(name: '_MockExamController.user', context: context);

  @override
  types.User? get user {
    _$userAtom.reportRead();
    return super.user;
  }

  @override
  set user(types.User? value) {
    _$userAtom.reportWrite(value, super.user, () {
      super.user = value;
    });
  }

  late final _$questionsAtom =
      Atom(name: '_MockExamController.questions', context: context);

  @override
  List<String>? get questions {
    _$questionsAtom.reportRead();
    return super.questions;
  }

  @override
  set questions(List<String>? value) {
    _$questionsAtom.reportWrite(value, super.questions, () {
      super.questions = value;
    });
  }

  late final _$answersAtom =
      Atom(name: '_MockExamController.answers', context: context);

  @override
  List<String>? get answers {
    _$answersAtom.reportRead();
    return super.answers;
  }

  @override
  set answers(List<String>? value) {
    _$answersAtom.reportWrite(value, super.answers, () {
      super.answers = value;
    });
  }

  late final _$durationsAtom =
      Atom(name: '_MockExamController.durations', context: context);

  @override
  List<String>? get durations {
    _$durationsAtom.reportRead();
    return super.durations;
  }

  @override
  set durations(List<String>? value) {
    _$durationsAtom.reportWrite(value, super.durations, () {
      super.durations = value;
    });
  }

  late final _$questionAtom =
      Atom(name: '_MockExamController.question', context: context);

  @override
  MockExamQuestionModel? get question {
    _$questionAtom.reportRead();
    return super.question;
  }

  @override
  set question(MockExamQuestionModel? value) {
    _$questionAtom.reportWrite(value, super.question, () {
      super.question = value;
    });
  }

  late final _$stateAtom =
      Atom(name: '_MockExamController.state', context: context);

  @override
  QuestionState get state {
    _$stateAtom.reportRead();
    return super.state;
  }

  @override
  set state(QuestionState value) {
    _$stateAtom.reportWrite(value, super.state, () {
      super.state = value;
    });
  }

  late final _$initAsyncAction =
      AsyncAction('_MockExamController.init', context: context);

  @override
  Future<void> init() {
    return _$initAsyncAction.run(() => super.init());
  }

  late final _$getNextQuestionAsyncAction =
      AsyncAction('_MockExamController.getNextQuestion', context: context);

  @override
  Future getNextQuestion(int questionIndex) {
    return _$getNextQuestionAsyncAction
        .run(() => super.getNextQuestion(questionIndex));
  }

  late final _$answerQuestionAsyncAction =
      AsyncAction('_MockExamController.answerQuestion', context: context);

  @override
  Future answerQuestion(String alternativeId, int questionIndex) {
    return _$answerQuestionAsyncAction
        .run(() => super.answerQuestion(alternativeId, questionIndex));
  }

  late final _$_MockExamControllerActionController =
      ActionController(name: '_MockExamController', context: context);

  @override
  void submmitExam() {
    final _$actionInfo = _$_MockExamControllerActionController.startAction(
        name: '_MockExamController.submmitExam');
    try {
      return super.submmitExam();
    } finally {
      _$_MockExamControllerActionController.endAction(_$actionInfo);
    }
  }

  @override
  String toString() {
    return '''
duration: ${duration},
user: ${user},
questions: ${questions},
answers: ${answers},
durations: ${durations},
question: ${question},
state: ${state},
time: ${time}
    ''';
  }
}
