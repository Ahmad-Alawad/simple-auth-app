# from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, request, flash, redirect, session
from model import db, User, connect_to_db #model is in current directory
import hashlib #Hashing Library
from authy.api import AuthyApiClient

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
authy_api = AuthyApiClient('MKBWUpWqL8CxUCTlXEUtCQnD6jPugvH9')

# app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """homepage."""
    return render_template("homepage.html")

@app.route('/signup')
def signup():
    """Sign up page."""
    return render_template("signup.html")

@app.route('/signup-form', methods=["POST"])
def signup_form():
    """Sign Up form processing"""
    email = request.form.get("email").lower() #to sanitize
    password = request.form.get("password")

    hashed_password = hashlib.md5()
    hashed_password.update(password)
    hashed_password = hashed_password.digest()

    # Create a user with email and password (hashed).
    user = User(email=email, password=hashed_password)

    # Add the user to database.
    db.session.add(user)
    db.session.commit()
    flash("You Signed Up Successfully! Please Sign In")

    return redirect("/")


@app.route('/signin', methods=["POST"])
def login():
    """Sign In form processing"""
    email = request.form.get("email")
    email = email.lower() #to sanitize
    password = request.form.get("password")

    try:
        # import pdb; pdb.set_trace()
        user = db.session.query(User).filter_by(email=email).one()
        user_password = user.password
        
        # Hash the password from login form
        hashed_password = hashlib.md5()
        hashed_password.update(password) 
        hashed_password = hashed_password.digest()
        if user_password.encode('utf-8') == hashed_password.decode('unicode_escape').encode('utf-8'):
            session['email'] = email
            return redirect('/phone-number')
        else:
            flash("Password doesn't match! Please try again!")
    except:
        flash("Email doesn't exist, please try agin!")

    return render_template("homepage.html")

@app.route('/phone-number')
def phone_number():
    """Enter phone number"""
    return render_template("phone_number.html")



@app.route('/phone-number-processing', methods=["POST"])
def phone_number_processing():
    """Phone number form processing"""
    phone_number = request.form.get("phonenumber")
    email = session['email']
    user = authy_api.users.create(email,phone_number,1)
    # import pdb; pdb.set_trace()
    if user.ok():
        authy_id = user.id
        sms = authy_api.users.request_sms(authy_id, {'force':True})
        session['authy_id'] = authy_id
        return redirect('/authy')      
    else:
        flash('Please try again!!!!')
        return redirect('/')
    

@app.route('/authy')
def authy():
    """Authy page."""
    return render_template("authy.html")


@app.route('/authy-verify', methods=["POST"])
def authy_verify():
    """Authy processing"""
    
    authycode = request.form.get("authycode")
    email = session['email']
    user_id = session['authy_id']
    verification = authy_api.tokens.verify(user_id, authycode)
    if verification.ok():
        flash("Logged in successfully!")
    else:
        flash("Verification code is not correct!")
    
    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug  
    connect_to_db(app)

    app.run(port=5001, host='0.0.0.0')