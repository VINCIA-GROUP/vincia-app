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

  late final _$chatIsOpenAtom =
      Atom(name: '_AdaptiveQuestionController.chatIsOpen', context: context);

  @override
  bool? get chatIsOpen {
    _$chatIsOpenAtom.reportRead();
    return super.chatIsOpen;
  }

  @override
  set chatIsOpen(bool? value) {
    _$chatIsOpenAtom.reportWrite(value, super.chatIsOpen, () {
      super.chatIsOpen = value;
    });
  }

  late final _$messagesAtom =
      Atom(name: '_AdaptiveQuestionController.messages', context: context);

  @override
  List<types.Message> get messages {
    _$messagesAtom.reportRead();
    return super.messages;
  }

  @override
  set messages(List<types.Message> value) {
    _$messagesAtom.reportWrite(value, super.messages, () {
      super.messages = value;
    });
  }

  late final _$userAtom =
      Atom(name: '_AdaptiveQuestionController.user', context: context);

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

  late final _$answerQuestionAsyncAction = AsyncAction(
      '_AdaptiveQuestionController.answerQuestion',
      context: context);

  @override
  Future<void> answerQuestion(dynamic alternativeId) {
    return _$answerQuestionAsyncAction
        .run(() => super.answerQuestion(alternativeId));
  }

  late final _$nextQuestionAsyncAction =
      AsyncAction('_AdaptiveQuestionController.nextQuestion', context: context);

  @override
  Future<void> nextQuestion() {
    return _$nextQuestionAsyncAction.run(() => super.nextQuestion());
  }

  late final _$handleSendPressedAsyncAction = AsyncAction(
      '_AdaptiveQuestionController.handleSendPressed',
      context: context);

  @override
  Future<void> handleSendPressed(types.PartialText message) {
    return _$handleSendPressedAsyncAction
        .run(() => super.handleSendPressed(message));
  }

  late final _$_AdaptiveQuestionControllerActionController =
      ActionController(name: '_AdaptiveQuestionController', context: context);

  @override
  void chatOpen() {
    final _$actionInfo = _$_AdaptiveQuestionControllerActionController
        .startAction(name: '_AdaptiveQuestionController.chatOpen');
    try {
      return super.chatOpen();
    } finally {
      _$_AdaptiveQuestionControllerActionController.endAction(_$actionInfo);
    }
  }

  @override
  String toString() {
    return '''
duration: ${duration},
question: ${question},
chatIsOpen: ${chatIsOpen},
messages: ${messages},
user: ${user},
state: ${state},
time: ${time}
    ''';
  }
}
