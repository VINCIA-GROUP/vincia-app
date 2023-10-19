# app/domain/entities/essay_rating.py
class EssayAdditionalText:
    def __init__(self, id: str, theme_id: str, content: str):
        self.id = id
        self.theme_id = theme_id  # Relates the additional text to a specific theme
        self.content = content
