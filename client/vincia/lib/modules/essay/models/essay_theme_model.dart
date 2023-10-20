// lib/modules/essay/models/essay_model.dart

class EssayTheme {
  final String id;
  final String title;
  final String tag;


  EssayTheme({
    required this.id,
    required this.title,
    required this.tag,

  });

  factory EssayTheme.fromJson(Map<String, dynamic> json) {
    return EssayTheme(
      id: json['id'],
      title: json['title'],
      tag: json['tag'],
    );
  }
}
