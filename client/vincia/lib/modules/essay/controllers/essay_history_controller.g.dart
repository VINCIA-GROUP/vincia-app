// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'essay_history_controller.dart';

// **************************************************************************
// StoreGenerator
// **************************************************************************

// ignore_for_file: non_constant_identifier_names, unnecessary_brace_in_string_interps, unnecessary_lambdas, prefer_expression_function_bodies, lines_longer_than_80_chars, avoid_as, avoid_annotating_with_dynamic, no_leading_underscores_for_local_identifiers

mixin _$EssayHistoryController on _EssayHistoryController, Store {
  late final _$essayHistoryFutureAtom = Atom(
      name: '_EssayHistoryController.essayHistoryFuture', context: context);

  @override
  ObservableFuture<List<Essay>>? get essayHistoryFuture {
    _$essayHistoryFutureAtom.reportRead();
    return super.essayHistoryFuture;
  }

  @override
  set essayHistoryFuture(ObservableFuture<List<Essay>>? value) {
    _$essayHistoryFutureAtom.reportWrite(value, super.essayHistoryFuture, () {
      super.essayHistoryFuture = value;
    });
  }

  late final _$essayAtom =
      Atom(name: '_EssayHistoryController.essay', context: context);

  @override
  List<Essay> get essay {
    _$essayAtom.reportRead();
    return super.essay;
  }

  @override
  set essay(List<Essay> value) {
    _$essayAtom.reportWrite(value, super.essay, () {
      super.essay = value;
    });
  }

  late final _$fetchEssayHistoryAsyncAction = AsyncAction(
      '_EssayHistoryController.fetchEssayHistory',
      context: context);

  @override
  Future<void> fetchEssayHistory() {
    return _$fetchEssayHistoryAsyncAction.run(() => super.fetchEssayHistory());
  }

  @override
  String toString() {
    return '''
essayHistoryFuture: ${essayHistoryFuture},
essay: ${essay}
    ''';
  }
}
