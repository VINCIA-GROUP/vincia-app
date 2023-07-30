from app.models.alternative import Alternative
from app.models.question import Question
from utils.db_manager import DatabaseManager

class AlternativeDAO():
    
   def get_alternatives_by_question(question: Question):
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM alternatives a WHERE a.question_id = %s;", (question.get_id(),))
         rows = db.cursor.fetchall()
         alternatives = []
         for row in rows:
            alternatives.append(Alternative(*row))
         return alternatives