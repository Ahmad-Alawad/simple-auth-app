from jinja2 import StrictUndefined
from flask import Flask, jsonify, render_template, request, flash, redirect

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return render_template("homepage.html")


@app.route('/login', methods=["POST"])
def login():
    """login form processing"""
    username = request.form.get("username")
    password = request.form.get("password")
    

    return render_template("homepage.html")


if __name__ == "__main__":
    app.debug = True

    # make sure templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug  

    app.run(port=5001, host='0.0.0.0')