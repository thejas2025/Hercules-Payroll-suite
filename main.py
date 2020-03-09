from flask import Flask
from flask import flash, redirect, render_template, request, session, abort,send_from_directory
import hashlib,sqlite3
conn = sqlite3.connect('HRsuite.db')

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


@app.route('/createHR/',methods=['POST'])
def createHRaccount():
    if request.method == 'POST':
        username = request.form['username']
        userid = request.form['userid']
        mailid = request.form['mail']
        password = request.form['password']
        hashed_pass = hashlib.md5(password.encode())
        hashed_pass = hashed_pass.hexdigest()
        cursor = conn.cursor()

        insert_into_HR_table = """INSERT INTO HR (userid,username,mailID,password) VALUES (?,?,?,?);"""
        data_tuple  =(userid,username,mailid,hashed_pass)
        cursor.execute(insert_into_HR_table, data_tuple)
        conn.commit()




        # print(username)
        # print(userid)
        # print(mailid)
        # print(password)
        # print(hashed_pass)

        return render_template('signup.html')


