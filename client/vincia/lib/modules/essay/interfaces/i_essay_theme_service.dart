// lib/modules/essay/services/essay_theme_service.dart
import '../models/essay_theme_model.dart';

abstract class IEssayThemeService {
  Future<List<EssayTheme>> getEssayTheme();
  Future<List<EssayTheme>> getRandomEssayTheme();
  Future<String> getUserId();
}
