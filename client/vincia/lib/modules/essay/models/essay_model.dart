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
      essayId: json['essayId'],
      userId: json['userId'],
      themeId: json['themeId'],
      title: json['title'],
      content: json['content'],
      datetime: DateTime.parse(json['datetime']),
      isFinished: json['isFinished'],
      c1Grade: json['c1Grade'].toDouble(),
      c2Grade: json['c2Grade'].toDouble(),
      c3Grade: json['c3Grade'].toDouble(),
      c4Grade: json['c4Grade'].toDouble(),
      c5Grade: json['c5Grade'].toDouble(),
      totalGrade: json['totalGrade'].toDouble(),
      c1Analysis: json['c1Analysis'],
      c2Analysis: json['c2Analysis'],
      c3Analysis: json['c3Analysis'],
      c4Analysis: json['c4Analysis'],
      c5Analysis: json['c5Analysis'],
      generalAnalysis: json['generalAnalysis'],
    );
  }

  DateTime get createdAt {
    return datetime;
  }
}
