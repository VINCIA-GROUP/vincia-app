# app/domain/entities/essay_theme.py
class EssayTheme:
    def __init__(self, theme_id: str, title: str, tag: str):
        self.theme_id = theme_id
        self.title = title
        self.tag = tag