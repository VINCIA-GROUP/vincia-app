from authlib.integrations.flask_oauth2 import current_token
from flask import abort

def verify_permissions(arguments):
    def wrapper(func):
        def func_decorate(*args, **kwargs):
            permissions = current_token['permissions']
            if arguments in permissions:
                result = func(*args, **kwargs)
                return result
            else:
                abort(403, description="ID inválido")
        return func_decorate
    return wrapper