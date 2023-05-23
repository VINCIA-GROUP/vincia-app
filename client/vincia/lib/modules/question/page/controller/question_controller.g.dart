// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'question_controller.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic, no_leading_underscores_for_local_identifiers

mixin _$QuestionController on _QuestionController, Store {
  Computed<String>? _$timeComputed;

  @override
  String get time => (_$timeComputed ??=
          Computed<String>(() => super.time, name: '_QuestionController.time'))
      .value;

  late final _$durationAtom =
      Atom(name: '_QuestionController.duration', context: context);

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

  late final _$questionAtom =
      Atom(name: '_QuestionController.question', context: context);

  @override
  QuestionModel? get question {
    _$questionAtom.reportRead();
    return super.question;
  }

  @override
  set question(QuestionModel? value) {
    _$questionAtom.reportWrite(value, super.question, () {
      super.question = value;
    });
  }

  late final _$stateAtom =
      Atom(name: '_QuestionController.state', context: context);

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
      AsyncAction('_QuestionController.init', context: context);

  @override
  Future<void> init() {
    return _$initAsyncAction.run(() => super.init());
  }

  late final _$_QuestionControllerActionController =
      ActionController(name: '_QuestionController', context: context);

  @override
  void answerQuestion(dynamic alternativeId) {
    final _$actionInfo = _$_QuestionControllerActionController.startAction(
        name: '_QuestionController.answerQuestion');
    try {
      return super.answerQuestion(alternativeId);
    } finally {
      _$_QuestionControllerActionController.endAction(_$actionInfo);
    }
  }

  @override
  String toString() {
    return '''
duration: ${duration},
question: ${question},
state: ${state},
time: ${time}
    ''';
  }
}
