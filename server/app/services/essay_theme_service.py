class EssayThemeService:

    def __init__(self, essay_theme_repository):
        self.essay_theme_repository = essay_theme_repository

    def get_all_themes(self):
        return self.essay_theme_repository.get_all()
    
    def get_theme_by_id(self, theme_id):
        return self.essay_theme_repository.get_by_id(theme_id)
    
    def get_random_theme(self):
        return self.essay_theme_repository.get_random_theme()
    
    def create_theme(self, theme_id, title, tag):
        return self.essay_theme_repository.insert_theme(theme_id, title, tag)
    
    def modify_theme(self, title, tag, theme_id):
        return self.essay_theme_repository.update_theme(title, tag, theme_id)
    
    def remove_theme(self, theme_id):
        return self.essay_theme_repository.delete_theme(theme_id)
