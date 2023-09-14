import 'package:vincia/modules/adaptive_question/model/alternative_model.dart';

class AdaptiveQuestionModel {
  String id;
  String statement;
  String answer;
  int difficulty;
  bool isEssay;
  List<AlternativeModel> alternatives = [];

  AdaptiveQuestionModel(this.id, this.statement, this.answer, this.difficulty,
      this.isEssay, this.alternatives);

  factory AdaptiveQuestionModel.fromJson(Map<String, dynamic> json) {
    var alternativesList = <AlternativeModel>[];

    var questionJson = json['question'];

    if (questionJson['alternatives'] != null) {
      var alternativesJson = questionJson['alternatives'] as List<dynamic>;
      alternativesList = alternativesJson
          .map((alternativeJson) => AlternativeModel.fromJson(alternativeJson))
          .toList();
    }

    return AdaptiveQuestionModel(
        questionJson['id'] as String,
        questionJson['statement'] as String,
        questionJson['answer'] as String,
        questionJson['rating'] as int,
        questionJson['is_essay'] as bool,
        alternativesList);
  }
}
