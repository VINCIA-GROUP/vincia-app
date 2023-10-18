# app/domain/entities/essay_rating.py
class EssayAdditionalText:
    def __init__(self, additional_text_id: str, theme_id: str, title: str, content: str):
        self.additional_text_id = additional_text_id
        self.theme_id = theme_id  # Relates the additional text to a specific theme
        self.content = content
