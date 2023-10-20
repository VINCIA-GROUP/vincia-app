import uuid

class EssayThemeService:

    def __init__(self, essay_theme_repository):
        self.essay_theme_repository = essay_theme_repository

    def get_all_themes(self):
        result = self.essay_theme_repository.get_all()
        self.essay_theme_repository.commit()
        return result
    
    def get_theme_by_id(self, theme_id):
        result = self.essay_theme_repository.get_by_id(theme_id)
        self.essay_theme_repository.commit()
        return result
    
    def get_random_theme(self):
        result = self.essay_theme_repository.get_random_theme()
        self.essay_theme_repository.commit()
        return result
    
    def create_theme(self, title, tag):
        result = self.essay_theme_repository.insert_theme(str(uuid.uuid4()), title, tag)
        self.essay_theme_repository.commit()
        return result
    
    def modify_theme(self, title, tag, theme_id):
        result = self.essay_theme_repository.update_theme(title, tag, theme_id)
        self.essay_theme_repository.commit()
        return result
    
    def remove_theme(self, theme_id):
        result = self.essay_theme_repository.delete_theme(theme_id)
        self.essay_theme_repository.commit()
        return result
