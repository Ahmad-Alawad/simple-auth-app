============================================
Simple App to test two-factor authentication
============================================

This application was created to implement the two-factor authentication for Twilio API Authy library.

IMPORTANT NOTES
---------------

- This application creates a Postgres database in your machine, so you need to have Postgres installed locally in order to run it.

Getting Started
---------------

To run this application on your local machine:

  ``git clone`` this repository on your machine.

Make a virtual environment for this project and install the dependencies::

  virtualenv env
  source env/bin/activate
  pip install -r requirements.txt

Create the model::
  
  python model.py

Run the server::
  
  python server.py

Open the application in your browser::

  Type: 0.0.0.0:5001 and hit Enter


Using the Application
---------------------

After you open the application in your broswer, you can try it following these steps:

- In the home page, you first need to sign up as a new user. After signing up, the application directs you back to homepage to sign in.

- Enter your email and password you used to sign up, and click "Sign In".

- The application will take you to the first authentication page, enter your phone number and country code (971 for UAE, 1 for USA, ....) the click "Send Code". 

- The application will take you to the authentication page.

- You will receive a seven digits security code (named JadoPado security code) on your phone. Enter the code to the input box and click "Verify".

- The application will take you back to the homepage and you will see a message that says "Logged in successfully!".
