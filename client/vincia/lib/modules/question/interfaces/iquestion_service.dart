import 'package:dartz/dartz.dart';

import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';
import '../model/question_model.dart';

abstract class IQuestionService {
  Future<Either<FailureModel, QuestionModel>> getQuestion();
  Future<Either<FailureModel, SuccessModel>> sendAnswerQuestion(
      String answer, Duration duration);
}
