import 'package:flutter/material.dart';
import 'package:flutter_modular/flutter_modular.dart';

class QuestionPage extends StatelessWidget {
  const QuestionPage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.close),
          onPressed: () {
            Modular.to.navigate("/home");
          },
        ),
        title: Center(
            child: Container(
                decoration: BoxDecoration(
                    border: Border.all(width: 1, color: Colors.black),
                    borderRadius: BorderRadius.circular(30)),
                padding:
                    const EdgeInsets.symmetric(vertical: 2.0, horizontal: 8.0),
                child: const Text(
                  "05:12 / 15:05",
                  style: TextStyle(fontSize: 16),
                ))),
        actions: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Container(
              decoration: BoxDecoration(
                  border: Border.all(width: 1, color: Colors.green),
                  borderRadius: BorderRadius.circular(30)),
              padding:
                  const EdgeInsets.symmetric(vertical: 2.0, horizontal: 8.0),
              child: const Text(
                "Fácil",
                style: TextStyle(color: Colors.green),
              ),
            ),
          )
        ],
      ),
      body: ListView(children: [
        _equestionStatement(),
        _alternatives(
          context,
          "A",
          'Ironia para conferir um novo Ironia para conferir um novo significado ao termo “outra coisa”.significado ao termo “outra coisa”',
          () {},
        ),
        _alternatives(
          context,
          "B",
          'Ironia para conferir um novo significado ao termo “outra coisa”.',
          () {},
        ),
        _alternatives(
          context,
          "C",
          'Homonímia para opor, a partir do advérbio de lugar, o espaço da população pobre e o espaço da população rica.',
          () {},
        ),
        _alternatives(
          context,
          "D",
          'Personificação para opor o mundo real pobre ao mundo virtual rico.',
          () {},
        ),
        _alternatives(
          context,
          "E",
          'Antonímia para comparar a rede mundial de computadores com a rede caseira de descanso da família.',
          () {},
        ),
      ]),
    );
  }

  Widget _equestionStatement() {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: Container(
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(10),
            boxShadow: [
              BoxShadow(
                color: Colors.grey.withOpacity(0.5),
                spreadRadius: 2,
                blurRadius: 5,
                offset: const Offset(8, 8),
              ),
            ],
          ),
          padding: const EdgeInsets.all(8.0),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: const [
              Text("(Enem 2012)"),
              Center(
                child: Image(
                  width: 250,
                  height: 250,
                  image: AssetImage("assets/images/enem-exemple.png"),
                ),
              ),
              Text(
                  "O efeito de sentido da charge é provocado pela combinação de informações visuais e recursos linguísticos. No contexto da ilustração, a frase proferida recorre à")
            ],
          )),
    );
  }

  Widget _alternatives(
      BuildContext context, String letter, String text, Function() onPressed) {
    return Padding(
      padding: const EdgeInsets.all(8.0),
      child: ElevatedButton(
        style: ElevatedButton.styleFrom(
          backgroundColor: Theme.of(context).colorScheme.primary,
          foregroundColor: Theme.of(context).colorScheme.onPrimary,
          shape: const RoundedRectangleBorder(
            borderRadius: BorderRadius.all(Radius.circular(10.0)),
          ),
        ),
        onPressed: onPressed,
        child: Padding(
          padding: const EdgeInsets.symmetric(vertical: 8.0),
          child: Row(
            children: [
              Padding(
                padding: const EdgeInsets.only(right: 8.0),
                child: Container(
                  decoration: BoxDecoration(
                    border: Border.all(
                      width: 1,
                      color: Theme.of(context).colorScheme.onPrimary,
                    ),
                    shape: BoxShape.circle,
                  ),
                  child: Padding(
                    padding: const EdgeInsets.all(8.0),
                    child: Text(letter),
                  ),
                ),
              ),
              Expanded(
                child: Text(
                  text,
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
