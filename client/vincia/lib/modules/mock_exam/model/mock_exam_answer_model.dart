class MockExamAnswerModel {
  List<String> answer;
  List<int> duration;
  List<int> ratings;
  List<String> correctAnwers;

  MockExamAnswerModel(this.answer, this.duration, this.ratings, this.correctAnwers);

  factory MockExamAnswerModel.fromJson(Map<String, dynamic> json) {
    final List<String> answerList = List<String>.from(json['answer']);
    final List<int> durationList = List<int>.from(json['duration']);
    final List<int> ratingsList = List<int>.from(json['ratings']);
    final List<String> correctAnwersList = List<String>.from(json['correctAnwers']);
    return MockExamAnswerModel(answerList, durationList, ratingsList, correctAnwersList);
  }

  Map<String, dynamic> toJson() {
    return {
      'answer': answer,
      'duration': duration,
      'ratings': ratings,
      'correctAnwers': correctAnwers,
    };
  }
}