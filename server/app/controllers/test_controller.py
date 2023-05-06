from flask import jsonify, request
from app import app, require_auth
from authlib.integrations.flask_oauth2 import current_token
from app.decorator.autentication_decorator import verify_permissions

@app.route("/api/public")
def public():
    """No access token required."""
    response = (
        "Hello from a public endpoint! You don't need to be"
        " authenticated to see this."
    )
    return jsonify(message=response)


@app.route("/api/private")
@require_auth(None)
def private():
    user_id = current_token.sub
    """A valid access token is required."""
    response = (
        f"Hello from a private endpoint! You need to be {user_id}"
    )
    return jsonify(message=response)


@app.route("/api/private-scoped")
@require_auth(None)
@verify_permissions("read:messages")
def private_scoped():
    """A valid access token and scope are required."""
    response = (
        "Hello from a private endpoint! You need to be"
        " authenticated and have a scope of read:messages to see"
        " this."
    )
    return jsonify(message=response)