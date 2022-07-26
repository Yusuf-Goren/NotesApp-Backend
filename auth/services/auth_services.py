
from asyncio import constants
from flask import jsonify, make_response, request, abort
from sqlalchemy import or_
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from model import User
from app import db, app
from http.client import BAD_REQUEST


def submit(request):
    username = request.json['userName']
    email = request.json['userEmail']

    user = User.query.filter(
        or_(User.username == username, User.email == email)).first()
    if(user.username == username):
        abort(make_response(
            jsonify({"message": "There is a user with this username!!!"}), BAD_REQUEST))
    if(user.email == email):
        abort(make_response(
            jsonify({"message": "You already registered with this e-mail"}), BAD_REQUEST))

    password = generate_password_hash(
        request.json['userPassword'], method='sha256')

    user = User(username, email, password)
    db.session.add(user)
    db.session.commit()
    return {'message': '.New User created'}


def login(request):
    auth = request.json
    print(auth)
    if not auth or not auth.get('userEmail') or not auth.get('userPassword'):

        return make_response(
            'Could not verify',
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

    user = User.query.filter_by(email=auth.get('userEmail')) .first()

    password = request.json['userPassword']
    if user:
        if check_password_hash(user.password, password):
            token = jwt.encode({'id': user.id, 'exp': datetime.datetime.utcnow(
            ) + datetime.timedelta(minutes=30000)}, app.config['SECRET_KEY'], algorithm="HS256")
            return jsonify({'token': token})

    print("Invalid identity")
    return "Invalid identity "
