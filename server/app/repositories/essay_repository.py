# app/repositories/essay_repository.py
from app.domain.entities.essay import Essay
from app.repositories.repository import Repository


class EssayRepository(Repository):
    def __init__(self, connection):
        super().__init__(connection, Essay)
    
    
    def get_by_id(self, id):
        essays = super().get_one(
            query="SELECT * FROM essays WHERE essay_id = %s;",
            params=(id,)
        )
        return essays
    
    def get_by_user_id(self, user_id):
        essays = super().get_many(
            query="SELECT * FROM essays WHERE user_id = %s;",
            params=(user_id,)
        )
        return essays
    
    def get_unfinished_by_user_id(self, user_id):
        essays = super().get_many(
            query="SELECT * FROM essays WHERE is_finished = %s AND user_id = %s;",
            params=("False",user_id,)
        )
        return essays
    
    def insert_new_essay(self, id, theme_id, user_id, title, contents, datetime, is_finished):
        print(f'essay_id: {id}, theme_id: {theme_id}, user_id: {user_id}')
        return super().update(
            query=("INSERT INTO essays (id, theme_id, user_id, title, contents, datetime, is_finished) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s);"),
            params=(id, theme_id, user_id, title, contents, datetime, is_finished)
        )
    
    def insert_essay(self, essay):
        return super().update(
            query=("INSERT INTO essays (id, theme_id, user_id, title, contents, datetime, is_finished, "
                   "c1_grade, c2_grade, c3_grade, c4_grade, c5_grade, total_grade, "
                   "c1_analysis, c2_analysis, c3_analysis, c4_analysis, c5_analysis, general_analysis) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"),
            params=(
                essay.id, essay.theme_id, essay.user_id, essay.title, essay.contents, essay.datetime, essay.is_finished,
                essay.c1_grade, essay.c2_grade, essay.c3_grade, essay.c4_grade, essay.c5_grade, essay.total_grade,
                essay.c1_analysis, essay.c2_analysis, essay.c3_analysis, essay.c4_analysis, essay.c5_analysis, essay.general_analysis
            )
        )

    def update_essay(self, essay):
        return super().update(
            query=("UPDATE essays SET theme_id=%s, user_id=%s, title=%s, contents=%s, datetime=%s, is_finished=%s, "
                   "c1_grade=%s, c2_grade=%s, c3_grade=%s, c4_grade=%s, c5_grade=%s, total_grade=%s, "
                   "c1_analysis=%s, c2_analysis=%s, c3_analysis=%s, c4_analysis=%s, c5_analysis=%s, general_analysis=%s "
                   "WHERE id=%s;"),
            params=(
                essay.theme_id, essay.user_id, essay.title, essay.contents, essay.datetime, essay.is_finished,
                essay.c1_grade, essay.c2_grade, essay.c3_grade, essay.c4_grade, essay.c5_grade, essay.total_grade,
                essay.c1_analysis, essay.c2_analysis, essay.c3_analysis, essay.c4_analysis, essay.c5_analysis, essay.general_analysis,
                essay.id
            )
        )

    def delete_essay(self, essay_id):
        return super().delete(
            query="DELETE FROM essays WHERE essay_id=%s;",
            params=(essay_id,)
        )
