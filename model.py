from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """Users table"""

    __tablename__ = "users"

    email = db.Column(db.String(64), primary_key=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)


def connect_to_db(app, db_uri=None):
    """Connect our application to our database."""

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri or 'postgres:///simpleauthappdb'
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
