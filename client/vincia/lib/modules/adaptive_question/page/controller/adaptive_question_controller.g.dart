// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'adaptive_question_controller.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic, no_leading_underscores_for_local_identifiers

mixin _$AdaptiveQuestionController on _AdaptiveQuestionController, Store {
  Computed<String>? _$timeComputed;

  @override
  String get time => (_$timeComputed ??= Computed<String>(() => super.time,
          name: '_AdaptiveQuestionController.time'))
      .value;

  late final _$durationAtom =
      Atom(name: '_AdaptiveQuestionController.duration', context: context);

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
      Atom(name: '_AdaptiveQuestionController.question', context: context);

  @override
  AdaptiveQuestionModel? get question {
    _$questionAtom.reportRead();
    return super.question;
  }

  @override
  set question(AdaptiveQuestionModel? value) {
    _$questionAtom.reportWrite(value, super.question, () {
      super.question = value;
    });
  }

  late final _$stateAtom =
      Atom(name: '_AdaptiveQuestionController.state', context: context);

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
      AsyncAction('_AdaptiveQuestionController.init', context: context);

  @override
  Future<void> init() {
    return _$initAsyncAction.run(() => super.init());
  }

  late final _$_AdaptiveQuestionControllerActionController =
      ActionController(name: '_AdaptiveQuestionController', context: context);

  @override
  void answerQuestion(dynamic alternativeId) {
    final _$actionInfo = _$_AdaptiveQuestionControllerActionController
        .startAction(name: '_AdaptiveQuestionController.answerQuestion');
    try {
      return super.answerQuestion(alternativeId);
    } finally {
      _$_AdaptiveQuestionControllerActionController.endAction(_$actionInfo);
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
