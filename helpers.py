
from functools import wraps
import jwt
import traceback
from flask import jsonify, request
from app import app
from model import User


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({'message': 'Token is missing !!'}), 401

        try:

            data = jwt.decode(
                token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = User.query.filter_by(
                id=data['id']).first()
        except:
            traceback.print_exc()
            return jsonify({
                'message': 'Token is invalid !!'
            }), 401

        return f(current_user, *args, **kwargs)

    return decorated
