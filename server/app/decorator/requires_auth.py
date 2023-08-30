
from app import app
from flask import request, session
import json
from urllib.request import urlopen
import jwt
from jwt.algorithms import RSAAlgorithm
import os
from app.domain.errors.authentication_errors import *
from app.domain.errors.api_exception import ApiException


def get_token_auth_header():
    """Obtains the access token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise ApiException(AuthorizationHeaderMissing())
    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise ApiException(InvalidHeaderToken())
    elif len(parts) == 1 and len(parts) > 2:
        raise ApiException(TokenNotFound())

    token = parts[1]
    return token

def requires_permissions(required_permissions, permissions):
    """Determines if the required premissions is present in the Access Token
    """
    if required_permissions == None or len(required_permissions) <= 0:
        return True
    for required_permission in required_permissions:
        if required_permission in permissions:
            return True
    return False

def requires_auth(permissions):
    def wrapper(func):
        def decorated(*args, **kwargs):      
                  
            AUTH0_DOMAIN = os.getenv("AUTH0_DOMAIN")
            API_AUDIENCE = os.getenv("AUDIENCE")
            
            token = get_token_auth_header()
            jsonurl = urlopen("https://"+AUTH0_DOMAIN+"/.well-known/jwks.json")
            jwks = json.loads(jsonurl.read())
            unverified_header = jwt.get_unverified_header(token)
            rsa_key = {}
            for key in jwks["keys"]:
                if key["kid"] == unverified_header["kid"]:
                    rsa_key = {
                        "kty": key["kty"],
                        "kid": key["kid"],
                        "use": key["use"],
                        "n": key["n"],
                        "e": key["e"]
                    }
            if rsa_key:
                try:
                    public_key = RSAAlgorithm.from_jwk(rsa_key)
                    payload = jwt.decode(
                        token,
                        public_key,
                        audience=API_AUDIENCE,
                        algorithms="RS256",
                        issuer="https://"+AUTH0_DOMAIN+"/"
                    )
                except jwt.ExpiredSignatureError:
                    raise ApiException(TokenExpired())
                except jwt.MissingRequiredClaimError:
                    raise ApiException(InvalidClaims())
                except Exception as e:
                    raise ApiException(InalidToken())
                    
                if(requires_permissions(permissions, payload.get("permissions"))):
                    session['current_user'] = payload
                else:
                    raise ApiException(PermissionDenid())
                
                return func(*args, **kwargs)
            raise ApiException(UnableFindKey())
        return decorated
    return wrapper