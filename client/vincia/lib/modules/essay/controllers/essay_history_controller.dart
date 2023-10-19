import 'package:mobx/mobx.dart';
import '../interfaces/i_essay_history_service.dart';
import '../models/essay_model.dart';

part 'essay_history_controller.g.dart';

class EssayHistoryController = _EssayHistoryController 
    with _$EssayHistoryController;

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
  
}
