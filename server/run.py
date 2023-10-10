from app import app
from waitress import serve
import os

if __name__ == "__main__":
    env = os.environ["API_ENVIRONMENT"]
    if(env == 'PRODUCTION'):
        serve(app, host="0.0.0.0", port=8080)
    else:
        app.run(debug=True, host='10.0.8.135', port=8080)
