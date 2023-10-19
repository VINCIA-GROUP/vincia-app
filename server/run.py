from app import app
from waitress import serve
import os

if __name__ == "__main__":
    env = os.environ["API_ENVIRONMENT"]
    if(env == 'PRODUCTION'):
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(debug=True, host='192.168.15.11', port=8080)
