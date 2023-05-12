
from app import AuthError, app
from flask import request, session
import json
from urllib.request import urlopen
import jwt
from jwt.algorithms import RSAAlgorithm
import os


def get_token_auth_header():
    """Obtains the access token from the Authorization Header
    """
    auth = request.headers.get("Authorization", None)
    if not auth:
        raise AuthError({"code": "authorization_header_missing",
                        "description":
                            "Authorization header is expected"}, 401)

    parts = auth.split()

    if parts[0].lower() != "bearer":
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must start with"
                            " Bearer"}, 401)
    elif len(parts) == 1:
        raise AuthError({"code": "invalid_header",
                        "description": "Token not found"}, 401)
    elif len(parts) > 2:
        raise AuthError({"code": "invalid_header",
                        "description":
                            "Authorization header must be"
                            " Bearer token"}, 401)

    token = parts[1]
    return token

def requires_permissions(required_permissions, permissions):
    """Determines if the required premissions is present in the Access Token
    """
    for required_permission in required_permissions:
        if required_permission in permissions:
            return True
    return False

def requires_auth(permissions):
    """Determines if the access token is valid
    """
    def wrapper(func):
        def decorated(*args, **kwargs):      
                  
            AUTH0_DOMAIN = os.environ["AUTH0_DOMAIN"]
            API_AUDIENCE = os.environ["AUDIENCE"]
            ALGORITHMS = os.environ["ALGORITHMS"]
            
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
                    raise AuthError({"code": "token_expired",
                                    "description": "token is expired"}, 401)
                except jwt.MissingRequiredClaimError:
                    raise AuthError({"code": "invalid_claims",
                                    "description":
                                        "incorrect claims,"
                                        "please check the audience and issuer"}, 401)
                except Exception as e:
                    raise AuthError({"code": "invalid_header",
                                    "description":
                                        "Unable to parse authentication"
                                        " token."}, 400)
                    
                if(requires_permissions(permissions, payload.get("permissions"))):
                    session['current_user'] = payload
                else:
                    raise AuthError({"code": "permission_denid",
                                    "description":
                                        "not permission"
                                        " token."}, 403)
                
                return func(*args, **kwargs)
            raise AuthError({"code": "invalid_header",
                            "description": "Unable to find appropriate key"}, 400)
        return decorated
    return wrapper