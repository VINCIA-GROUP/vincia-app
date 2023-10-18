//lib/modules/essay/interfaces/i_essay_history_service.dart

import 'package:dartz/dartz.dart';
import '../../../shared/model/failure_model.dart';
import '../../../shared/model/success_model.dart';
import '../models/essay_model.dart';

abstract class IEssayHistoryService {
  Future<List<Essay>> getEssayHistory();
  Future<String> getUserId();
}
