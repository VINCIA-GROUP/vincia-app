class MockExamAnswerModel {
  String answer;
  Duration duration;
  int difficulty;

  MockExamAnswerModel(this.answer, this.duration, this.difficulty);

  factory MockExamAnswerModel.fromJson(Map<String, dynamic> json) {
    return MockExamAnswerModel(
      json['answer'] as String,
      Duration(milliseconds: json['duration'] as int),
      json['difficulty'] as int
      );
    }

  Map<String, dynamic> toJson() {
    return {
      'answer': answer,
      'duration': duration,
      'difficulty': difficulty
    };
  }
}