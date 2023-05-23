class AlternativeModel {
  String id;
  String text;

  AlternativeModel(this.id, this.text);

  factory AlternativeModel.fromJson(Map<String, dynamic> json) {
    return AlternativeModel(
      json['id'] as String,
      json['text'] as String,
    );
  }
}
