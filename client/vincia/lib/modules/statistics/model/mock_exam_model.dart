class MockExam {
  DateTime created_at;
  Duration duration;
  Map<String, double> grades;
  double general_grade;
  double bestPerformance;
  double worstPerformance;

  MockExam({
    required this.created_at,
    required this.duration,
    required this.grades,
    required this.general_grade,
  }) : bestPerformance = 0.0,
        worstPerformance = double.infinity {
    bestPerformance = grades.values.reduce((max, grade) => grade > max ? grade : max);
    worstPerformance = grades.values.reduce((min, grade) => grade < min ? grade : min);
  }
}

String getSubjectName(MockExam exam, double performance) {
  for (var entry in exam.grades.entries) {
    if (entry.value == performance) {
      return entry.key;
    }
  }
  return 'Matéria Desconhecida'; // Caso não encontre a matéria
}
