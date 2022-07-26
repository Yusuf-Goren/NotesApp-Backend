

from auth.services import auth_services
from flask import Blueprint, request
AUTH = Blueprint('AUTH', __name__)


@AUTH.post("/login")
def login():
    response = auth_services.login(request)
    return response


@AUTH.post("/submit")
def submit():
    response = auth_services.submit(request)
    return response
