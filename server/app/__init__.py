import os

from dotenv import load_dotenv
from flask import Flask
from authlib.integrations.flask_oauth2 import ResourceProtector
from app.validators.auth_validator import Auth0JWTBearerTokenValidator

load_dotenv()

require_auth = ResourceProtector()
validator = Auth0JWTBearerTokenValidator(
    "dev-zqwk5k31wg11dtkh.us.auth0.com",
    "vincia-api-v1"
)

require_auth.register_token_validator(validator)

app = Flask(__name__)

from app.controllers import test_controller