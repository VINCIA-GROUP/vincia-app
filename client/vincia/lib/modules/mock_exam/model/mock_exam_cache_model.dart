import 'package:vincia/modules/mock_exam/model/mock_exam_alternative_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';

class MockExamCacheModel {
  String id;
  int area;
  String statement;
  List<MockExamAlternativeModel> alternatives;
  String answer;
  bool isEssay;
  int rating;
  String answered;
  Duration duration;

  MockExamCacheModel({
    required this.id, 
    required this.area,
    required this.statement, 
    required this.alternatives, 
    required this.answer, 
    required this.isEssay, 
    required this.rating, 
    required this.answered, 
    required this.duration
  });

  static MockExamCacheModel fromMap(Map<String, dynamic> map) {
    return MockExamCacheModel(
      id: map['id'],
      area: map['area'],
      statement: map['statement'],
      alternatives: map['alternatives'],
      answer: map['answer'],
      isEssay: map['is_essay'],
      rating: map['rating'],
      answered: map['answered'],
      duration: map['duration'],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'area': area,
      'statement': statement,
      'alternatives': alternatives,
      'answer': answer,
      'is_essay': isEssay,
      'rating': rating,
      'answered': answered,
      'duration': duration,
    };
  }

  MockExamQuestionModel toQuestion() {
    return MockExamQuestionModel(
      id, 
      statement, 
      answer, 
      rating, 
      isEssay, 
      alternatives
    );
  }
}