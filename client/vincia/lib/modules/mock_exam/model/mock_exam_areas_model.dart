import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';

class MockExamAreasModel {
  List<MockExamQuestionModel> humanities = [];
  List<MockExamQuestionModel> naturalScience = [];
  List<MockExamQuestionModel> languages = [];
  List<MockExamQuestionModel> mathematics = [];

  MockExamAreasModel(this.humanities, this.naturalScience, this.languages, this.mathematics);

  factory MockExamAreasModel.fromJson(Map<String, dynamic> json) {
    var humanities = <MockExamQuestionModel>[];
    var humanitiesJson = json['humanities'] as List<dynamic>;
    humanities = humanitiesJson.map(
      (question) => MockExamQuestionModel.fromJson(question)
    ).toList();

    var naturalScience = <MockExamQuestionModel>[];
    var naturalScienceJson = json['natural_science'] as List<dynamic>;
    naturalScience = naturalScienceJson.map(
      (question) => MockExamQuestionModel.fromJson(question)
    ).toList();

    var languages = <MockExamQuestionModel>[];
    var languagesJson = json['languages'] as List<dynamic>;
    languages = languagesJson.map(
      (question) => MockExamQuestionModel.fromJson(question)
    ).toList();

    var mathematics = <MockExamQuestionModel>[];
    var mathematicsJson = json['mathematics'] as List<dynamic>;
    mathematics = mathematicsJson.map(
      (question) => MockExamQuestionModel.fromJson(question)
    ).toList();

    return MockExamAreasModel(
      humanities, 
      naturalScience, 
      languages, 
      mathematics
    );
  }
}