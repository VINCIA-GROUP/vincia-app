from app import app
from app import connection
from flask import request

@app.teardown_request
def terminate_request(exception):
    print("!!!!!!!!!")
    connection.rollback()
