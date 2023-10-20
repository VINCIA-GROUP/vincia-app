# app/domain/entities/essay_theme.py
class EssayTheme:
    def __init__(self, id: str, title: str, tag: str):
        self.id = id
        self.title = title
        self.tag = tag

    def to_json(self):
        return {
            "id": self.id,
            "title": self.title,
            "tag": self.tag
        }