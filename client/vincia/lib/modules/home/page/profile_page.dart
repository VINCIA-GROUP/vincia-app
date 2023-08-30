import 'package:flutter/material.dart';
import 'package:flutter_mobx/flutter_mobx.dart';
import 'package:flutter_modular/flutter_modular.dart';

import 'controller/profile_controller.dart';

class ProfilePage extends StatelessWidget {
  final ProfileController _profileController = Modular.get<ProfileController>();

  ProfilePage({super.key}) {
    _profileController.init();
  }

  @override
  Widget build(BuildContext context) {
    // id, name, email, email verified, updated_at
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          icon: const Icon(Icons.close),
          onPressed: () => Modular.to.pop(),
        ),
      ),
      body: Observer(builder: (context) {
        var user = _profileController.user;
        var pictureUrl = user?.pictureUrl;
        return Padding(
          padding: const EdgeInsets.all(8.0),
          child:
              Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            if (pictureUrl != null)
              Center(
                child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    child: CircleAvatar(
                      radius: 56,
                      child:
                          ClipOval(child: Image.network(pictureUrl.toString())),
                    )),
              ),
            Card(
                child: Column(children: [
              _userEntryWidget(propertyName: 'Id', propertyValue: user?.sub),
              _userEntryWidget(propertyName: 'Name', propertyValue: user?.name),
              _userEntryWidget(
                  propertyName: 'Email', propertyValue: user?.email),
              _userEntryWidget(
                  propertyName: 'Email Verified?',
                  propertyValue: user?.isEmailVerified.toString()),
              _userEntryWidget(
                  propertyName: 'Updated at',
                  propertyValue: user?.updatedAt?.toIso8601String()),
            ])),
          ]),
        );
      }),
    );
  }

  Widget _userEntryWidget(
      {required String propertyName, String? propertyValue}) {
    return Container(
        padding: const EdgeInsets.all(6),
        child: Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [Text(propertyName), Text(propertyValue ?? '')],
        ));
  }
}
