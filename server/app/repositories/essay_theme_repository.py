# app/repositories/essay_theme_repository.py
from app.domain.entities.essay_theme import EssayTheme
from app.repositories.repository import Repository


class EssayThemeRepository(Repository):
    def __init__(self, connection):
        super().__init__(connection, EssayTheme)

    def get_all(self):
        return super().get_many(
            query="SELECT * FROM essay_themes;",
            params=""
        )

    def get_by_id(self, theme_id):
        return super().get_one(
            query="SELECT * FROM essay_themes WHERE theme_id = %s;",
            params=(theme_id,)
        )
    
    def get_random_theme(self):
        return super().get_one(
            query="SELECT * FROM essay_themes ORDER BY RANDOM() LIMIT 1;",
            params=""
        )

    def insert_theme(self, theme_id, title, tag):
        return super().insert(
            query="INSERT INTO essay_themes (theme_id, title, tag) VALUES (%s, %s, %s);",
            params=(theme_id, title, tag)
        )

    def update_theme(self, title, tag, theme_id):
        return super().update(
            query="UPDATE essay_themes SET title=%s, tag=%s WHERE theme_id=%s;",
            params=(title, tag, theme_id)
        )

    def delete_theme(self, theme_id):
        return super().delete(
            query="DELETE FROM essay_themes WHERE theme_id=%s;",
            params=(theme_id,)
        )  
