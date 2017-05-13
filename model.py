from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """Users table"""

    __tablename__ = "users"

    email = db.Column(db.String(150), primary_key=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)


def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///simpleauthappdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":

    # To create the database in the system
    import os
    os.system('createdb simpleauthappdb')

    # to connect app to db
    from server import app
    connect_to_db(app)
    print "Connected to DB."

    # create all tables in the database
    db.create_all()