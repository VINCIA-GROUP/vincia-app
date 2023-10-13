import 'package:vincia/modules/mock_exam/model/mock_exam_alternative_model.dart';
import 'package:vincia/modules/mock_exam/model/mock_exam_question_model.dart';

class MockExamCacheModel {
  String id;
  String area;
  String? statement;
  List<MockExamAlternativeModel>? alternatives;
  String? answer;
  bool? isEssay;
  int? rating;
  String? answered;
  Duration? duration;

  MockExamCacheModel({
    required this.id, 
    required this.area,
    this.statement, 
    this.alternatives, 
    this.answer, 
    this.isEssay, 
    this.rating, 
    this.answered, 
    this.duration
  });

  static MockExamCacheModel fromCacheMap(Map<String, dynamic> map) {
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

  static MockExamCacheModel fromDBMap(Map<String, dynamic> map, String area, String? answered, Duration? duration) {
    return MockExamCacheModel(
      id: map['id'],
      area: area,
      statement: map['statement'],
      alternatives: map['alternatives'],
      answer: map['answer'],
      isEssay: map['is_essay'],
      rating: map['rating'],
      answered: answered,
      duration: duration,
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
      statement!, 
      answer!, 
      rating!, 
      isEssay!, 
      alternatives!
    );
  }
}