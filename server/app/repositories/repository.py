from psycopg2 import DatabaseError

class Repository():
    def __init__(self, connection):
        self.connection = connection

    def get_one(self, query, params, result_type):
        result = result_type()
        error = ""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if (len(cursor) > 0):
                row = cursor.fetchone()
                result = result_type(*row)
            else:
                error = 'Não existem dados para essa consulta'
            cursor.close()
        except DatabaseError as error:
            error = error
        return (result, error)

    def get_many(self, query, params, result_type):
        result = []
        error = ""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if (len(cursor) > 0):
                rows = cursor.fetchall()
                for row in rows:
                    obj = result_type(*row)
                    result.append(obj)
            else:
                error = 'Não existem dados para essa consulta'
            cursor.close()
        except DatabaseError as error:
            error = error
        return (result, error)

    def update(self, query, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            cursor.close()
            return (True, "")
        except DatabaseError as error:
            return (False, error)

    def commit(self):
        try:
            self.connection.commit()
            return (True, "")
         except DatabaseError as error:
            return (False, error)
      
   def rollback(self):
        try:
            self.connection.rollback()
            return (True, "")
        except DatabaseError as error:
            return (False, error)