# app/domain/entities/essay.py
from typing import Optional
from datetime import datetime
from typing import Optional

class Essay:
    def __init__(
        self,
        essay_id: int,
        user_id: str,
        theme_id: str,
        title: str,
        content: str,
        datetime: datetime,
        is_finished: bool,
        c1_grade: Optional[float] = None,
        c2_grade: Optional[float] = None,
        c3_grade: Optional[float] = None,
        c4_grade: Optional[float] = None,
        c5_grade: Optional[float] = None,
        total_grade: Optional[float] = None,
        c1_analysis: Optional[str] = None,
        c2_analysis: Optional[str] = None,
        c3_analysis: Optional[str] = None,
        c4_analysis: Optional[str] = None,
        c5_analysis: Optional[str] = None,
        general_analysis: Optional[str] = None
    ):
        self.essay_id = essay_id
        self.user_id = user_id
        self.theme_id = theme_id
        self.title = title
        self.content = content
        self.datetime = datetime
        self.is_finished = is_finished
        self.c1_grade = c1_grade
        self.c2_grade = c2_grade
        self.c3_grade = c3_grade
        self.c4_grade = c4_grade
        self.c5_grade = c5_grade
        self.total_grade = total_grade
        self.c1_analysis = c1_analysis
        self.c2_analysis = c2_analysis
        self.c3_analysis = c3_analysis
        self.c4_analysis = c4_analysis
        self.c5_analysis = c5_analysis
        self.general_analysis = general_analysis
