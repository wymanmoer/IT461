from flask import jsonify, request, current_app
import jwt
import datetime

from v1.user.model import UserModel


def jwt_token_required():
    token = request.args.get("token")
    if not token:
        return jsonify({"message": "Token is required"}), 403
    if not verify_token(token):
        return jsonify({"message": "Token is invalid or expired"}), 403


def verify_token(token):
    try:
        decoded_token = jwt.decode(
            token, current_app.config["SECRET_KEY"], algorithms="HS256"
        )
    except:
        return False
    return decoded_token


def login(username, password):
    model = UserModel()
    user = model.read(filters={"username": username, "password": password})

    if user:
        payload = {
            "username": username,
            "id": 100,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=24),
        }
        token = jwt.encode(payload, current_app.config["SECRET_KEY"], algorithm="HS256")
        return token
    return False