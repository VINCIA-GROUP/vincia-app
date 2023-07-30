import os
import psycopg2

class DatabaseManager:
   def __init__(self):
      cs = os.environ["CONNECTION_STRING_DB"]
      self.conn = psycopg2.connect(cs)
      self.cursor = self.conn.cursor()

   def __enter__(self):
      return self
   
   def __exit__(self, exc_type, exc_value, traceback):
      self.conn.commit()
      self.conn.close()

