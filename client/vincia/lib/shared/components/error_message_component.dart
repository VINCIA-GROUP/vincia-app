import 'package:flutter/material.dart';

import '../errors/error_model.dart';

class ErrorMessageComponent {
  static void showAlertDialog(
      BuildContext context, List<ErrorModel> errorList, Function onPressed) {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      showDialog(
          barrierDismissible: false,
          context: context,
          builder: (_) {
            return errorList.length < 2
                ? dialogAlertUniqueMessage(context, errorList[0], onPressed)
                : dialogAlertMultiMessage(context, errorList, onPressed);
          });
    });
  }

  static void showSnackBar(BuildContext context, String message) {
    WidgetsBinding.instance.addPostFrameCallback((_) {
      ScaffoldMessenger.of(context).showSnackBar(SnackBar(
        content: Text(message),
      ));
    });
  }

  static Widget dialogAlertUniqueMessage(
      BuildContext context, ErrorModel error, Function onPressed) {
    return AlertDialog(
      title: Text("Error: ${error.code}"),
      content: Text(error.message),
      actions: [
        TextButton(onPressed: () => onPressed(), child: const Text("OK"))
      ],
    );
  }

  static Widget dialogAlertMultiMessage(
      BuildContext context, List<ErrorModel> errorList, Function onPressed) {
    return AlertDialog(
      content: ListView.builder(
          itemCount: errorList.length,
          itemBuilder: (BuildContext context, int index) {
            var error = errorList[index];
            return Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(
                  "Error: ${error.code}",
                  style: const TextStyle(fontWeight: FontWeight.bold),
                ),
                Text(error.message),
                const SizedBox(
                  height: 8,
                )
              ],
            );
          }),
      actions: [
        TextButton(onPressed: () => onPressed(), child: const Text("OK"))
      ],
    );
  }
}
