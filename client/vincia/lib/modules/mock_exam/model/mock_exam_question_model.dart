import 'package:vincia/modules/mock_exam/model/mock_exam_alternative_model.dart';

class MockExamQuestionModel {
  String id;
  String statement;
  String answer;
  int difficulty;
  bool isEssay;
  List<MockExamAlternativeModel> alternatives = [];

  MockExamQuestionModel(this.id, this.statement, this.answer, this.difficulty, this.isEssay, this.alternatives);

  factory MockExamQuestionModel.fromJson(Map<String, dynamic> json) {
    var alternativesList = <MockExamAlternativeModel>[];
    var alternativesJson = json['alternatives'] as List<dynamic>;
    alternativesList = alternativesJson.map(
      (alternativeJson) => MockExamAlternativeModel.fromJson(alternativeJson)
    ).toList();

    return MockExamQuestionModel(
      json['id'] as String, 
      json['statement'] as String, 
      json['answer'] as String, 
      json['rating'] as int, 
      json['is_essay'] as bool,
      alternativesList
    );
  }
}