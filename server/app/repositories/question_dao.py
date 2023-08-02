from app.models.question import Question
from app.dao.alternative_dao import AlternativeDAO
from utils.db_manager import DatabaseManager

class QuestionDAO():

   def get_all_questions():
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM questions;")
         rows = db.cursor.fetchall()
         questions = []
         for row in rows:
            question = Question(*row)
            alternatives = AlternativeDAO.get_alternatives_by_question(question)
            question.set_alternatives(alternatives)
            questions.append(question)
         return questions

   def get_question_by_id(self, id):
      with DatabaseManager() as db:
         db.cursor.execute("SELECT * FROM questions q WHERE q.id = %s;", (id,))
         row = db.cursor.fetchall()[0]
         question = Question(*row)
         alternatives = AlternativeDAO.get_alternatives_by_question(question)
         question.set_alternatives(alternatives)
         return question

   def get_filtered_questions(filters): #filter_example = {"rating": "> 1.0", "is_essay": "= false"}
      with DatabaseManager() as db:
         query = "SELECT * FROM questions q WHERE "
         questions = []
         conditions = []
         if filters:
            for column, filter in filters.items():
               condition = f"{column} {filter}"
               conditions.append(condition)
         query += " AND ".join(condition)
         db.cursor.execute(query)
         rows = db.cursor.fetchall()
         for row in rows:
            question = Question(*row)
            alternatives = AlternativeDAO.get_alternatives_by_question(question)
            question.set_alternatives(alternatives)
            questions.append(question)
         return questions