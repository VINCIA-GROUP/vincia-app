from flask import jsonify, request, session
from app import app
from app.decorator.requires_auth import requires_auth
from app.controllers.base_controller import *
from app.domain.errors import api_exception
from app.domain.errors.authentication_errors import AuthorizationHeaderMissing

@app.route("/api/test/public", endpoint="test/public")
def public():
    """No access token required."""
    print("Ola")
    response = (
        "Hello from a public endpoint! You don't need to be"
        " authenticated to see this."
    )
    return success_api_response(response)



@app.route("/api/test/private", endpoint="test/private")
@requires_auth(permissions=["read:messages","write:messages"])
def private():
    user_id = session.get('current_user').get('sub')
    """A valid access token is required."""
    response = (
        f"Hello from a private endpoint! You need to be {user_id}"
    )
    return success_api_response(response)



# @app.route("/api/private-scoped")
# @requires_auth("write")
# @verify_permissions("read:messages")
# def private_scoped():
#     """A valid access token and scope are required."""
#     response = (
#         "Hello from a private endpoint! You need to be"
#         " authenticated and have a scope of read:messages to see"
#         " this."
#     )
#     return jsonify(message=response)