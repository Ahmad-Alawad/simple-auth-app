from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, request, flash, redirect, session
from model import db, User #model is in current directory
import hashlib #Hashing Library

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """homepage."""
    return render_template("homepage.html")

@app.route('/signup')
def signup():
    """homepage."""
    return render_template("signup.html")

@app.route('/signup-form', methods=["POST"])
def sign_up():
    """Sign form processing"""
    email = request.form.get("email").lower() #to sanitize
    password = request.form.get("password")

    try:
        user = db.session.query(User).filter(username=username).one()
        user_password = user.password
        # Hash the password from login form
        hashed_password = hashlib.md5()
        hashed_password.update(password) 

        if hashed_password == user_password:
            session['user'] = email
            flash("Logged in successfully!")
        else:
            flash("Password doesn't match! Please try again!")
    except :
        flash("Email doesn't exist, please try agin!")

    return render_template("homepage.html")

@app.route('/signin', methods=["POST"])
def login():
    """login form processing"""
    email = request.form.get("email").lower() #to sanitize
    password = request.form.get("password")

    try:
        user = db.session.query(User).filter(username=username).one()
        user_password = user.password
        # Hash the password from login form
        hashed_password = hashlib.md5()
        hashed_password.update(password) 

        if hashed_password == user_password:
            session['user'] = email
            flash("Logged in successfully!")
        else:
            flash("Password doesn't match! Please try again!")
    except :
        flash("Email doesn't exist, please try agin!")

    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True

    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug  

    app.run(port=5001, host='0.0.0.0')