from http.client import BAD_REQUEST
from flask import abort, jsonify, make_response, request
from platformdirs import user_state_dir
from model import Note
from app import db


def get_notes(current_user):
    items = []
    for item in Note.query.filter_by(user_id=current_user.id).order_by(Note.id).all():
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)
    return jsonify(items)


def create_note(current_user, request):
    title = request.json['title']
    text = request.json['text']
    if len(text) < 3 or len(title) < 3:
        abort(make_response(
            jsonify({"message": "Title and Text should have at least 3 letters!!!"}), BAD_REQUEST))

    note = Note(title, text, user_id=current_user.id)
    db.session.add(note)
    db.session.commit()
    return {'message': 'Note created!'}


def edit_note(current_user, note_id, request):
    text_updated = request.json['text']
    title_updated = request.json['title']
    db.session.query(Note).filter_by(id=note_id).update(
        dict(title=title_updated, text=text_updated)
    )
    db.session.commit()
    return {'message': 'Note edited!'}


def find_note(current_user, request):
    items = []
    searchtext = request.json['searchText']
    searchtext = f"%{searchtext}%"
    for item in Note.query.filter(Note.user_id == current_user.id, Note.text.ilike(searchtext)).all():
        print(item.title)
        del item.__dict__['_sa_instance_state']
        items.append(item.__dict__)

    return jsonify(items)


def delete_note(current_user, note_id):
    db.session.query(Note).filter(Note.id == note_id).delete()
    db.session.commit()
    return(note_id)
