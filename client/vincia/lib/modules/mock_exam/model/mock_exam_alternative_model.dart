class MockExamAlternativeModel {
  String id;
  String text;

  MockExamAlternativeModel(this.id, this.text);

  factory MockExamAlternativeModel.fromJson(Map<String, dynamic> json) {
    return MockExamAlternativeModel(
      json['id'] as String,
      json['text'] as String,
    );
  }
}
