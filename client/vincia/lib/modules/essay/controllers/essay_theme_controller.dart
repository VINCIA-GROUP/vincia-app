import 'package:mobx/mobx.dart';
import '../interfaces/i_essay_theme_service.dart';
import '../models/essay_theme_model.dart';

part 'essay_theme_controller.g.dart';

class EssayThemeController = _EssayThemeController 
    with _$EssayThemeController;

abstract class _EssayThemeController with Store {
  final IEssayThemeService _essayThemeService;
  final essays = <EssayTheme>[];

  _EssayThemeController(this._essayThemeService);

  @observable
  ObservableFuture<List<EssayTheme>>? essayThemeFuture;

  @observable
  List<EssayTheme> essaytheme = [];

  @action
  Future<void> fetchEssayTheme() async {
    essayThemeFuture = ObservableFuture(_essayThemeService.getEssayTheme());
    var result = await _essayThemeService.getEssayTheme();
    essaytheme = List.from(essaytheme..addAll(result));
  }

  @action
  Future<void> fetchRandomEssayTheme() async {
    essayThemeFuture = ObservableFuture(_essayThemeService.getRandomEssayTheme());
    var result = await _essayThemeService.getRandomEssayTheme();
    essaytheme = List.from(essaytheme..addAll(result));
  }
}
