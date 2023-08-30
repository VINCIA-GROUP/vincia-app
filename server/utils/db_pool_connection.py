import os
import psycopg2
import psycopg2.pool

class DatabaseConnection:
   def __init__(self, min_connections=1, max_connections=10):
      connection_string = os.getenv("CONNECTION_STRING_DB")
      self._pool = psycopg2.pool.ThreadedConnectionPool(
         minconn=min_connections,
         maxconn=max_connections,
         dsn=connection_string
      )

   def get_connection(self):
      connection = self._pool.getconn()
      return connection
   
   def release_connection(self, connection):
      self._pool.putconn(connection)

   def close_connections(self):
      self._pool.closeall()