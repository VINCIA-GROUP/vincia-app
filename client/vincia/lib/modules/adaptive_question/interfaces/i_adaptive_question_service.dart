import 'package:dartz/dartz.dart';

import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';
import '../model/adaptive_question_model.dart';

abstract class IAdaptiveQuestionService {
  Future<Either<FailureModel, AdaptiveQuestionModel>> getQuestion();
  Future<Either<FailureModel, SuccessModel>> sendAnswerQuestion(
      String answer, Duration duration);
}
