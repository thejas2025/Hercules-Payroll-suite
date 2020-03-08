from flask import Flask
from flask import flash, redirect, render_template, request, session, abort,send_from_directory


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/about/')
def aboutpage():
    return render_template('about.html')

@app.route('/signup/')
def signUpPageForHRs():
    return render_template('signup.html')

@app.route('/login/')
def loginPageForHRs():
    return render_template('login.html')