from app.domain.entities.essay_additional_texts import EssayAdditionalText
from app.repositories.repository import Repository


class EssayAdditionalTextRepository(Repository):
    def __init__(self, connection):
        super().__init__(connection, EssayAdditionalText)
    

    def get_by_id(self, text_id): 
        return super().get_one(
            query="SELECT * FROM essay_additional_texts WHERE text_id = %s;",
            params=(text_id,)
        )
    
    def get_by_theme_id(self, theme_id):
        return super().get_many(
            query="SELECT * FROM essay_additional_texts WHERE theme_id = %s;",
            params=(theme_id,)
        )
    
    def insert_additional_text(self, additional_text_id, theme_id, title, content):
        return super().insert(
            query="INSERT INTO essay_additional_texts (text_id, theme_id, title, content) VALUES (%s, %s, %s, %s);",
            params=(additional_text_id, theme_id, title, content)
        )
    
    def update_additional_text(self, theme_id, title, content, text_id):
        return super().update(
            query="UPDATE essay_additional_texts SET theme_id=%s, title=%s, content=%s WHERE text_id=%s;",
            params=(theme_id, title, content, text_id)
        )

    def delete_additional_text(self, text_id):
        return super().delete(
            query="DELETE FROM essay_additional_texts WHERE text_id=%s;",
            params=(text_id,)
        )
