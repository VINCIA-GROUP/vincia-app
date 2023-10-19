//lib/modules/essay/interfaces/i_essay_history_service.dart
import '../models/essay_model.dart';

abstract class IEssayHistoryService {
  Future<List<Essay>> getEssayHistory();
  Future<String> getUserId();
}
