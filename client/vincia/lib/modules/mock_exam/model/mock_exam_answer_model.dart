class MockExamAnswerModel {
  String answer;
  Duration duration;

  MockExamAnswerModel(this.answer, this.duration);

  factory MockExamAnswerModel.fromJson(Map<String, dynamic> json) {
    return MockExamAnswerModel(
      json['answer'] as String,
      Duration(milliseconds: json['duration'] as int),
      );
    }

  Map<String, dynamic> toJson() {
    return {
      'answer': answer,
      'duration': duration,
    };
  }
}