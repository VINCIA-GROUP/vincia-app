// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'essay_theme_controller.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic, no_leading_underscores_for_local_identifiers

mixin _$EssayThemeController on _EssayThemeController, Store {
  late final _$essayThemeFutureAtom =
      Atom(name: '_EssayThemeController.essayThemeFuture', context: context);

  @override
  ObservableFuture<List<EssayTheme>>? get essayThemeFuture {
    _$essayThemeFutureAtom.reportRead();
    return super.essayThemeFuture;
  }

  @override
  set essayThemeFuture(ObservableFuture<List<EssayTheme>>? value) {
    _$essayThemeFutureAtom.reportWrite(value, super.essayThemeFuture, () {
      super.essayThemeFuture = value;
    });
  }

  late final _$essaythemeAtom =
      Atom(name: '_EssayThemeController.essaytheme', context: context);

  @override
  List<EssayTheme> get essaytheme {
    _$essaythemeAtom.reportRead();
    return super.essaytheme;
  }

  @override
  set essaytheme(List<EssayTheme> value) {
    _$essaythemeAtom.reportWrite(value, super.essaytheme, () {
      super.essaytheme = value;
    });
  }

  late final _$fetchEssayThemeAsyncAction =
      AsyncAction('_EssayThemeController.fetchEssayTheme', context: context);

  @override
  Future<void> fetchEssayTheme() {
    return _$fetchEssayThemeAsyncAction.run(() => super.fetchEssayTheme());
  }

  @override
  String toString() {
    return '''
essayThemeFuture: ${essayThemeFuture},
essaytheme: ${essaytheme}
    ''';
  }
}
