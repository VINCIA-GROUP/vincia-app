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
  List<List<MockExamCacheModel>>? get questions {
    _$questionsAtom.reportRead();
    return super.questions;
  }

  @override
  set questions(List<List<MockExamCacheModel>>? value) {
    _$questionsAtom.reportWrite(value, super.questions, () {
      super.questions = value;
    });
  }

  late final _$questionAtom =
      Atom(name: '_MockExamController.question', context: context);

  @override
  MockExamCacheModel? get question {
    _$questionAtom.reportRead();
    return super.question;
  }

  @override
  set question(MockExamCacheModel? value) {
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

  late final _$_MockExamControllerActionController =
      ActionController(name: '_MockExamController', context: context);

  @override
  dynamic getNextQuestion(int qArea, int qPosition) {
    final _$actionInfo = _$_MockExamControllerActionController.startAction(
        name: '_MockExamController.getNextQuestion');
    try {
      return super.getNextQuestion(qArea, qPosition);
    } finally {
      _$_MockExamControllerActionController.endAction(_$actionInfo);
    }
  }

  @override
  void answerQuestion(dynamic alternativeId, int qArea, int qPosition) {
    final _$actionInfo = _$_MockExamControllerActionController.startAction(
        name: '_MockExamController.answerQuestion');
    try {
      return super.answerQuestion(alternativeId, qArea, qPosition);
    } finally {
      _$_MockExamControllerActionController.endAction(_$actionInfo);
    }
  }

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
question: ${question},
state: ${state},
time: ${time}
    ''';
  }
}
