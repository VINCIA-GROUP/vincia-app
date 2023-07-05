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

    if (json['alternatives'] != null) {
      var alternativesJson = json['alternatives'] as List<dynamic>;
      alternativesList = alternativesJson
          .map((alternativeJson) => AlternativeModel.fromJson(alternativeJson))
          .toList();
    }

    return AdaptiveQuestionModel(
      json['id'] as String,
      json['statement'] as String,
      json['answer'] as String,
      json['difficulty'] as int,
      json['is_essay'] as bool,
      alternativesList,
    );
  }
}
