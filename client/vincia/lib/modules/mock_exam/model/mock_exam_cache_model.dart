class MockExamCacheModel {
  int id;
  String statement;
  String alternatives;
  String answer;
  bool is_essay;
  int rating;
  String answered;
  Duration duration;

  MockExamCacheModel({
    required this.id, 
    required this.statement, 
    required this.alternatives, 
    required this.answer, 
    required this.is_essay, 
    required this.rating, 
    required this.answered, 
    required this.duration
  });

  static MockExamCacheModel fromMap(Map<String, dynamic> map) {
    return MockExamCacheModel(
      id: map['id'],
      statement: map['statement'],
      alternatives: map['alternatives'],
      answer: map['answer'],
      is_essay: map['is_essay'],
      rating: map['rating'],
      answered: map['answered'],
      duration: map['duration'],
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'id': id,
      'statement': statement,
      'alternatives': alternatives,
      'answer': answer,
      'is_essay': is_essay,
      'rating': rating,
      'answered': answered,
      'duration': duration,
    };
  }
}