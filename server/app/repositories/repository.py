from psycopg2 import DatabaseError

class Repository():
    def __init__(self, connection, entity):
        self.connection = connection
        self.entity = entity

    def get_one(self, query, params):
        data = self.entity()
        error = ""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if (len(cursor) > 0):
                row = cursor.fetchone()
                data = self.entity(*row)
            else:
                error = 'Não existem dados para essa consulta'
            cursor.close()
        except DatabaseError as error:
            print(self.__class__.__name__ + ' - ' + error.pgerror)
        return data

    def get_many(self, query, params):
        data = []
        error = ""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            if (len(cursor) > 0):
                rows = cursor.fetchall()
                for row in rows:
                    obj = self.entity(*row)
                    data.append(obj)
            else:
                error = 'Não existem dados para essa consulta'
            cursor.close()
        except DatabaseError as error:
            print(self.__class__.__name__ + ' - ' + error.pgerror)
        return data

    def update(self, query, params):
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            cursor.close()
            return True
        except DatabaseError as error:
            print(self.__class__.__name__ + ' - ' + error.pgerror)
            return False

    def commit(self):
        try:
            self.connection.commit()
            return True
        except DatabaseError as error:
            print(self.__class__.__name__ + ' - ' + error.pgerror)
            return False
      
    def rollback(self):
        try:
            self.connection.rollback()
            return True
        except DatabaseError as error:
            print(self.__class__.__name__ + ' - ' + error.pgerror)
            return False