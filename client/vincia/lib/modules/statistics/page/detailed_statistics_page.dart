import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:vincia/modules/statistics/model/mock_exam_model.dart';
import 'package:vincia/util/color_schemes.dart';

class DetailedStatisticsPage extends StatelessWidget {
  final MockExam exam;

  DetailedStatisticsPage(this.exam);

  @override
  Widget build(BuildContext context) {
    final brazilianDateFormat = DateFormat('dd/MM/yyyy');
    final formattedDate = brazilianDateFormat.format(exam.created_at);
    final formattedDuration =
        '${exam.duration.inHours}h ${exam.duration.inMinutes.remainder(60)}min';

    String bestSubject = getSubjectName(exam, exam.bestPerformance);
    String worstSubject = getSubjectName(exam, exam.worstPerformance);

    Map<String, Color> subjectColors = {
      'Linguagens e Códigos': Colors.red,
      'Ciências Humanas': Colors.blue,
      'Ciências da Natureza': Colors.green,
      'Matemática': Colors.amber,
    };

    // Mapa de ícones para cada matéria
    Map<String, IconData> subjectIcons = {
      'Linguagens e Códigos': Icons.language,
      'Ciências Humanas': Icons.people,
      'Ciências da Natureza': Icons.eco,
      'Matemática': Icons.calculate,
    };

    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Detalhes',
          style: TextStyle(
            color: Colors.white,
            fontSize: 24.0,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: lightColorScheme.primary,
      ),
      body: Container(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            SizedBox(height: 16),
            Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  'Simulado feito em: $formattedDate',
                  style: TextStyle(
                      fontSize: 25.0,
                      fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 8),
                Text(
                  'Duração: $formattedDuration',
                  style: TextStyle(
                      fontSize: 25.0,
                      fontWeight: FontWeight.bold,
                  ),
                ),
              ],
            ),
            Expanded(child: SizedBox()),

            Column(
              children: [
                Text(
                  'Notas por Matéria:',
                  style: TextStyle(
                      fontSize: 25.0,
                      fontWeight: FontWeight.bold,
                  ),
                ),
                SizedBox(height: 8),
                Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: exam.grades.entries.map((entry) {
                    return Row(
                      children: [
                        Icon(subjectIcons[entry.key] ?? Icons.book),
                        SizedBox(width: 10),
                        Text(
                          '${entry.key}: ${entry.value.toStringAsFixed(0)}', // Alteração aqui para remover as casas decimais
                          style: TextStyle(
                            fontSize: 22.0,
                            color: subjectColors[entry.key] ?? Colors.black,
                            fontWeight: FontWeight.bold,
                          ),
                        ),
                      ],
                    );
                  }).toList(),
                ),
              ],
            ),
            Expanded(child: SizedBox()),

            Center(
              child: Text(
                'Nota Geral: ${exam.general_grade.toStringAsFixed(0)}', // Alteração aqui para remover as casas decimais
                style: TextStyle(
                    fontSize: 40.0,
                    fontWeight: FontWeight.bold,
                    color: Colors.black),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
