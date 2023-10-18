# app/repositories/essay_repository.py
from app.domain.entities.essay import Essay
from app.repositories.repository import Repository


class EssayRepository(Repository):
    def __init__(self, connection):
        super().__init__(connection, Essay)
    
    
    def get_by_id(self, id):
        return super().get_one(
            query="SELECT * FROM essays WHERE essay_id = %s;",
            params=(id,)
        )
    
    def get_by_user_id(self, user_id):
        return super().get_many(
            query="SELECT * FROM essays WHERE user_id = %s;",
            params=(user_id,)
        )
    
    def get_unfinished(self):
        return super().get_many(
            query="SELECT * FROM essays WHERE is_finished = %s;",
            params=(False,)
    )
    
    def insert_essay(self, essay):
        return super().insert(
            query=("INSERT INTO essays (user_id, theme_id, title, content, datetime, is_finished, "
                   "c1_grade, c2_grade, c3_grade, c4_grade, c5_grade, total_grade, "
                   "c1_analysis, c2_analysis, c3_analysis, c4_analysis, c5_analysis, general_analysis) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"),
            params=(
                essay.user_id, essay.theme_id, essay.title, essay.content, essay.datetime, essay.is_finished,
                essay.c1_grade, essay.c2_grade, essay.c3_grade, essay.c4_grade, essay.c5_grade, essay.total_grade,
                essay.c1_analysis, essay.c2_analysis, essay.c3_analysis, essay.c4_analysis, essay.c5_analysis, essay.general_analysis
            )
        )
    
    def update_essay(self, essay):
        return super().update(
            query=("UPDATE essays SET user_id=%s, theme_id=%s, title=%s, content=%s, datetime=%s, is_finished=%s, "
                   "c1_grade=%s, c2_grade=%s, c3_grade=%s, c4_grade=%s, c5_grade=%s, total_grade=%s, "
                   "c1_analysis=%s, c2_analysis=%s, c3_analysis=%s, c4_analysis=%s, c5_analysis=%s, general_analysis=%s "
                   "WHERE essay_id=%s;"),
            params=(
                essay.user_id, essay.theme_id, essay.title, essay.content, essay.datetime, essay.is_finished,
                essay.c1_grade, essay.c2_grade, essay.c3_grade, essay.c4_grade, essay.c5_grade, essay.total_grade,
                essay.c1_analysis, essay.c2_analysis, essay.c3_analysis, essay.c4_analysis, essay.c5_analysis, essay.general_analysis,
                essay.essay_id
            )
        )

    def delete_essay(self, essay_id):
        return super().delete(
            query="DELETE FROM essays WHERE essay_id=%s;",
            params=(essay_id,)
        )
