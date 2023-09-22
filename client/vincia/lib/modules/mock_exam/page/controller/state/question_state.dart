import 'package:vincia/shared/model/failure_model.dart';

abstract class QuestionState {}

class InitialState extends QuestionState {}

class AnsweredQuestionState extends QuestionState {
  final String alternativeId;
  AnsweredQuestionState(this.alternativeId);
}

class FailureState extends QuestionState {
  final FailureModel failure;
  FailureState(this.failure);
}
