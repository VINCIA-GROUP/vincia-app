class EssayAdditionalTextService:

    def __init__(self, essay_additional_text_repository):
        self.essay_additional_text_repository = essay_additional_text_repository

    def get_additional_text_by_id(self, text_id):
        return self.essay_additional_text_repository.get_by_id(text_id)
    
    def get_additional_texts_by_theme_id(self, theme_id):
        return self.essay_additional_text_repository.get_by_theme_id(theme_id)
    
    def create_additional_text(self, additional_text_id, theme_id, title, content):
        return self.essay_additional_text_repository.insert_additional_text(additional_text_id, theme_id, title, content)
    
    def modify_additional_text(self, theme_id, title, content, text_id):
        return self.essay_additional_text_repository.update_additional_text(theme_id, title, content, text_id)
    
    def remove_additional_text(self, text_id):
        return self.essay_additional_text_repository.delete_additional_text(text_id)
