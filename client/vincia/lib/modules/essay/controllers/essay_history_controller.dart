import 'package:mobx/mobx.dart';
import '../interfaces/i_essay_history_service.dart';
import '../models/essay_model.dart';

part 'essay_history_controller.g.dart';

class EssayHistoryController = _EssayHistoryController with _$EssayHistoryController;

abstract class _EssayHistoryController with Store {
  final IEssayHistoryService _essayHistoryService;
  final essays = <Essay>[];

  _EssayHistoryController(this._essayHistoryService);

  @observable
  ObservableFuture<List<Essay>>? essayHistoryFuture;

  @observable
  List<Essay> essay = [];

  @action
  Future<void> fetchEssayHistory() async {
    essayHistoryFuture = ObservableFuture(_essayHistoryService.getEssayHistory());
    var result = await _essayHistoryService.getEssayHistory();
    essay = List.from(essay..addAll(result));
  }

  @action
  Future<void> fetchUnfinishedEssay() async {
    essayHistoryFuture = ObservableFuture(_essayHistoryService.getUnfinishedEssay());
    var result = await _essayHistoryService.getUnfinishedEssay();
    essay = List.from(essay..addAll(result));
  }

  @action
Future<Essay> createEssay(Map<String, dynamic> essayData) async {
  try {
    final Essay newEssay = await _essayHistoryService.createEssay(essayData);
    essay = List.from(essay..add(newEssay));
    // Optionally, you might want to update the essayHistoryFuture
    // essayHistoryFuture = ObservableFuture.value(List.from(essay));
    return newEssay;
  } catch (e) {
    // Handle error, e.g., by logging or showing a user-friendly error message
    print('Failed to create essay: $e');
    throw e;
  }
}
}
