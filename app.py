from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/notesapp'
app.config['SECRET_KEY'] = 'secretKey'


db = SQLAlchemy()

with app.app_context():
    from auth.controllers.auth_controller import AUTH
    from notes.controllers.notes_controller import NOTE

    db.init_app(app)
    db.create_all()
    db.session.commit()
    migrate = Migrate(app, db)

    app.register_blueprint(AUTH, url_prefix='/')
    app.register_blueprint(NOTE, url_prefix='/')


if __name__ == "__main__":
    app.run(debug=True)
