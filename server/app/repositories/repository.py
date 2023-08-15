from psycopg2 import DatabaseError

from app.domain.errors.api_exception import ApiException
from app.domain.errors.domain_errors import DataNotFound

class Repository():
    def __init__(self, connection, model):
        self.connection = connection
        self.model = model

    def get_one(self, query, params):
        data = None
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        if(cursor.rowcount <= 0):
            cursor.close()
            return data
        row = cursor.fetchone()
        data = self.model(*row)
        cursor.close()
        return data

    def get_many(self, query, params):
        data = []
        error = ""
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        if(cursor.rowcount <= 0):
            cursor.close()
            return data
        rows = cursor.fetchall()
        for row in rows:
            obj = self.model(*row)
            data.append(obj)
        cursor.close()
        return data

    def update(self, query, params):
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        cursor.close()

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()