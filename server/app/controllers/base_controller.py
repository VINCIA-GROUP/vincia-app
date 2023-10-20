from flask import jsonify

def success_api_response(data):
    return jsonify(sucess= True, data= data)
