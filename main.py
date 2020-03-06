from flask import Flask
from flask import flash, redirect, render_template, request, session, abort,send_from_directory


app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

