from notes.services import notes_services
from flask import Blueprint, request
from helpers import token_required
NOTE = Blueprint('NOTE', __name__)


@NOTE.get("/note/user")
@token_required
def get_user_notes(current_user):
    response = notes_services.get_notes(current_user)
    return response


@NOTE.post("/write")
@token_required
def create_note(current_user):
    response = notes_services.create_note(current_user, request)
    return response


@NOTE.put("/edit/<note_id>")
@token_required
def edit_note(current_user, note_id):
    response = notes_services.edit_note(current_user, note_id, request)
    return response


@NOTE.post("/note")
@token_required
def find_note(current_user):
    response = notes_services.find_note(current_user, request)
    return response


@NOTE.delete("/delete/<note_id>")
@token_required
def delete_note(current_user, note_id):
    print(note_id)
    response = notes_services.delete_note(current_user, note_id)
    return response
