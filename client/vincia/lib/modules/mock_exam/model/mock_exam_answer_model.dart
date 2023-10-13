class MockExamAnswerModel {
  List<String> answer;
  List<String> duration;

  MockExamAnswerModel(this.answer, this.duration);

  factory MockExamAnswerModel.fromJson(Map<String, dynamic> json) {
    final List<String> answerList = List<String>.from(json['answer']);
    final List<String> durationList = List<String>.from(json['duration']);
    return MockExamAnswerModel(answerList, durationList);
  }

  Map<String, dynamic> toJson() {
    return {
      'answer': answer,
      'duration': duration,
    };
  }
}