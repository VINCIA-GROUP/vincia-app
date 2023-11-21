// lib/modules/essay/models/essay_model.dart

class Essay {
  final String essayId;
  final String userId;
  final String themeId;
  final String title;
  final String content;
  final DateTime datetime;
  final bool isFinished;
  final double c1Grade;
  final double c2Grade;
  final double c3Grade;
  final double c4Grade;
  final double c5Grade;
  final double totalGrade;
  final String c1Analysis;
  final String c2Analysis;
  final String c3Analysis;
  final String c4Analysis;
  final String c5Analysis;
  final String generalAnalysis;

  Essay({
    required this.essayId,
    required this.userId,
    required this.themeId,
    required this.title,
    required this.content,
    required this.datetime,
    required this.isFinished,
    required this.c1Grade,
    required this.c2Grade,
    required this.c3Grade,
    required this.c4Grade,
    required this.c5Grade,
    required this.totalGrade,
    required this.c1Analysis,
    required this.c2Analysis,
    required this.c3Analysis,
    required this.c4Analysis,
    required this.c5Analysis,
    required this.generalAnalysis,
  });

  factory Essay.fromJson(Map<String, dynamic> json) {
  return Essay(
    essayId: json['id'] ?? '',
    userId: json['user_id'] ?? '',
    themeId: json['theme_id'] ?? '',
    title: json['title'] ?? '',
    content: json['content'] ?? '',
    datetime: DateTime.parse(json['datetime']),
    isFinished: json['is_finished'],
    c1Grade: (json['c1_grade'] ?? 0).toDouble(),
    c2Grade: (json['c2_grade'] ?? 0).toDouble(),
    c3Grade: (json['c3_grade'] ?? 0).toDouble(),
    c4Grade: (json['c4_grade'] ?? 0).toDouble(),
    c5Grade: (json['c5_grade'] ?? 0).toDouble(),
    totalGrade: (json['total_grade'] ?? 0).toDouble(),
    c1Analysis: json['c1_analysis'] ?? '',
    c2Analysis: json['c2_analysis'] ?? '',
    c3Analysis: json['c3_analysis'] ?? '',
    c4Analysis: json['c4_analysis'] ?? '',
    c5Analysis: json['c5_analysis'] ?? '',
    generalAnalysis: json['general_analysis'] ?? '',
  );
}

  DateTime get createdAt {
    return datetime;
  }
}
