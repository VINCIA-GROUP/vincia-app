import 'package:flutter/material.dart';
import 'package:vincia/modules/statistics/model/mock_exam_model.dart';
import 'package:intl/intl.dart';
import 'package:vincia/util/color_schemes.dart';
import 'package:vincia/modules/statistics/page/detailed_statistics_page.dart';
import 'dart:math';
import 'package:fl_chart/fl_chart.dart';

class StatisticsPage extends StatelessWidget {
  final random = Random();
  final DateTime initialDate = DateTime(2023, 10, 12);
  final List<MockExam> exams = [
    MockExam(
      created_at: DateTime(2023, 10, 12),
      duration: Duration(hours: 4, minutes: 37),
      grades: {
        'Linguagens e Códigos': 850.0,
        'Ciências Humanas': 783.0,
        'Ciências da Natureza': 875.0,
        'Matemática': 920.0,
      },
      general_grade: 857.0,
    ),
    MockExam(
      created_at: DateTime(2023, 10, 24),
      duration: Duration(hours: 4, minutes: 56),
      grades: {
        'Linguagens e Códigos': 890.0,
        'Ciências Humanas': 783.0,
        'Ciências da Natureza': 875.0,
        'Matemática': 930.0,
      },
      general_grade: 870.0,
    ),
    MockExam(
      created_at: DateTime(2023, 9, 5),
      duration: Duration(hours: 4, minutes: 45),
      grades: {
        'Linguagens e Códigos': 850.0,
        'Ciências Humanas': 780.0,
        'Ciências da Natureza': 890.0,
        'Matemática': 840.0,
      },
      general_grade: 840.0,
    ),
    MockExam(
      created_at: DateTime(2023, 8, 18),
      duration: Duration(hours: 4, minutes: 30),
      grades: {
        'Linguagens e Códigos': 800.0,
        'Ciências Humanas': 810.0,
        'Ciências da Natureza': 850.0,
        'Matemática': 830.0,
      },
      general_grade: 823.0,
    ),
    MockExam(
      created_at: DateTime(2023, 7, 30),
      duration: Duration(hours: 4, minutes: 20),
      grades: {
        'Linguagens e Códigos': 790.0,
        'Ciências Humanas': 740.0,
        'Ciências da Natureza': 820.0,
        'Matemática': 820.0,
      },
      general_grade: 793.0,
    ),
    MockExam(
      created_at: DateTime(2023, 7, 12),
      duration: Duration(hours: 4, minutes: 50),
      grades: {
        'Linguagens e Códigos': 760.0,
        'Ciências Humanas': 780.0,
        'Ciências da Natureza': 760.0,
        'Matemática': 790.0,
      },
      general_grade: 773.0,
    ),
    MockExam(
      created_at: DateTime(2023, 6, 25),
      duration: Duration(hours: 4, minutes: 40),
      grades: {
        'Linguagens e Códigos': 740.0,
        'Ciências Humanas': 780.0,
        'Ciências da Natureza': 720.0,
        'Matemática': 810.0,
      },
      general_grade: 763.0,
    ),
    MockExam(
      created_at: DateTime(2023, 6, 7),
      duration: Duration(hours: 4, minutes: 25),
      grades: {
        'Linguagens e Códigos': 730.0,
        'Ciências Humanas': 760.0,
        'Ciências da Natureza': 690.0,
        'Matemática': 780.0,
      },
      general_grade: 740.0,
    ),
  ];


  StatisticsPage();

  @override
  Widget build(BuildContext context) {
    final brazilianDateFormat = DateFormat('dd/MM/yyyy');
    exams.sort((a, b) => b.created_at.compareTo(a.created_at));
    final List<Color> colors = [Colors.red, Colors.blue, Colors.green, Colors.yellow];
    final List<String> subjects = ['Linguagens e Códigos', 'Ciências Humanas', 'Ciências da Natureza', 'Matemática'];

    Widget legendWidget = Column(
      children: [
        for (int i = 0; i < subjects.length; i += 2)
          Row(
            children: [
              Padding(
                padding: EdgeInsets.symmetric(horizontal: 8.0),
                child: Row(
                  children: [
                    Container(
                      width: 12,
                      height: 12,
                      color: colors[i],
                    ),
                    SizedBox(width: 4),
                    Container(
                      width: 150, // Largura fixa para os textos
                      child: Text(subjects[i]),
                    ),
                  ],
                ),
              ),
              if (i + 1 < subjects.length)
                Padding(
                  padding: EdgeInsets.symmetric(horizontal: 8.0),
                  child: Row(
                    children: [
                      Container(
                        width: 12,  // Largura fixa para as caixas de cor
                        height: 12, // Altura fixa para as caixas de cor
                        color: colors[i + 1],
                      ),
                      SizedBox(width: 4),
                      Container(
                        width: 150, // Largura fixa para os textos
                        child: Text(subjects[i + 1]),
                      ),
                    ],
                  ),
                ),
            ],
          ),
      ],
    );

    Widget chartWidget = Container(
      width: double.infinity,
      height: 300, // Ajuste a altura conforme necessário
      child: LineChart(
        LineChartData(
          gridData: FlGridData(show: false),
          titlesData: FlTitlesData(
            bottomTitles: SideTitles(
              showTitles: true,
              getTitles: (value) { // Colocar creted_at
                return '';
              },
            ),
          ),
          borderData: FlBorderData(show: true),
          minX: exams.length - 1.0,
          maxX: 0,
          minY: 680,
          maxY: 1000.0, // Ajuste o valor máximo conforme suas notas
          lineBarsData: createChartData(exams),
        ),
      ),
    );

    return Scaffold(
      appBar: AppBar(
        title: Text(
          'Estatísticas',
          style: TextStyle(
            color: Colors.white,
            fontSize: 24.0,
            fontWeight: FontWeight.bold,
          ),
        ),
        centerTitle: true,
        backgroundColor: lightColorScheme.primary,
      ),
      body: Column(
        children: [
          chartWidget,
          legendWidget,
          Expanded(
            child: ListView(
              children: exams.map((exam) {
                final formattedDate = brazilianDateFormat.format(exam.created_at);
                final formattedDuration = '${exam.duration.inHours}h ${exam.duration.inMinutes.remainder(60)}min';
                final formattedGrade = exam.general_grade.toInt().toString();

                return Card(
                  margin: EdgeInsets.all(8.0),
                  color: lightColorScheme.primaryContainer,
                  child: InkWell(
                    onTap: () {
                      Navigator.of(context).push(
                        MaterialPageRoute(
                          builder: (context) => DetailedStatisticsPage(exam),
                        ),
                      );
                    },
                    child: Column(
                      children: [
                        ListTile(
                          title: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            children: [
                              Text(
                                formattedDate,
                                style: TextStyle(
                                  color: lightColorScheme.onSurface,
                                ),
                              ),
                              Row(
                                children: [
                                  Icon(Icons.access_time, color: lightColorScheme.primary),
                                  Text(
                                    formattedDuration,
                                    style: TextStyle(
                                      color: lightColorScheme.onSurface,
                                    ),
                                  ),
                                ],
                              ),
                              Text(
                                formattedGrade,
                                style: TextStyle(
                                  color: lightColorScheme.onSurface,
                                  fontWeight: FontWeight.bold,
                                  fontSize: 30.0,
                                ),
                              ),
                            ],
                          ),
                        ),
                        Align(
                          alignment: Alignment.bottomLeft,
                          child: Padding(
                            padding: EdgeInsets.all(8.0),
                            child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start,
                              children: [
                                Text(
                                  'Melhor desempenho: ${getSubjectName(exam, exam.bestPerformance)}',
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 16,
                                    color: lightColorScheme.primary,
                                  ),
                                ),
                                Text(
                                  'Pior desempenho: ${getSubjectName(exam, exam.worstPerformance)}',
                                  style: TextStyle(
                                    fontWeight: FontWeight.bold,
                                    fontSize: 16,
                                    color: lightColorScheme.primary,
                                  ),
                                ),
                              ],
                            ),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              }).toList(),
            ),
          ),
        ],
      ),
    );
  }
}

// Crie uma lista de dados de notas ao longo do tempo para cada disciplina
List<LineChartBarData> createChartData(List<MockExam> exams) {
  final List<LineChartBarData> chartData = [];
  final List<Color> colors = [
    Colors.red,       // Cor para 'Linguagens e Códigos'
    Colors.blue,      // Cor para 'Ciências Humanas'
    Colors.green,     // Cor para 'Ciências da Natureza'
    Colors.yellow,    // Cor para 'Matemática'
  ];

  // Crie um conjunto de dados para cada disciplina
  for (int i = 0; i < colors.length; i++) {
    final subject = ['Linguagens e Códigos', 'Ciências Humanas', 'Ciências da Natureza', 'Matemática'][i];
    final List<FlSpot> data = [];

    // Preencha os pontos de dados com as notas ao longo do tempo
    for (int j = 0; j < exams.length; j++) {
      final exam = exams[j];
      data.add(FlSpot(j.toDouble(), exam.grades[subject]?.toDouble() ?? 0.0));
    }

    // Crie um conjunto de dados com os pontos de dados
    chartData.add(
      LineChartBarData(
        spots: data,
        isCurved: true,
        colors: [colors[i]], // Cor da linha do gráfico
        belowBarData: BarAreaData(show: false),
        barWidth: 4.0,
      ),
    );
  }

  return chartData;
}

