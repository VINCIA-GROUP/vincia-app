import 'package:vincia/shared/model/failure_model.dart';

abstract class QuestionState {}

class InitialState extends QuestionState {}

class AnsweredQuestionState extends QuestionState {
  final bool isCorrect;
  final String alternativeId;
  AnsweredQuestionState(this.isCorrect, this.alternativeId);
}

class FailureState extends QuestionState {
  final FailureModel failure;
  FailureState(this.failure);
}
