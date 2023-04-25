import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/container.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:vincia_app/util/color_schemes.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Vincia")),
      body: FloatingActionButton(
        onPressed: () => {},
        child: Icon(Icons.access_time_sharp),
      ),
    );
  }
}
