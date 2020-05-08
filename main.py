from flask import Flask
from flask import flash, redirect, render_template, request, session, abort,send_from_directory,url_for
from werkzeug.utils import secure_filename
from os.path import join,dirname,realpath
import csv
import hashlib,sqlite3,smtplib


# UPLOAD_FOLDER = join(dirname(realpath(__file__)), 'dataset/')
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.secret_key = "RandomStringIsRequiredAsASecretKey"


# Default home page of the application.
@app.route('/')
def homepage():
    return render_template('index.html')

#About page. Information about teammates.
@app.route('/about/')
def aboutpage():
    return render_template('about.html')

#Signup page for admins.
@app.route('/signup/')
def signUpPageForHRs():
    return render_template('signup.html')

#Register/Sign up for admins will be handled in the below route.
@app.route('/createHR/',methods=['POST'])
def createHRaccount():
    with sqlite3.connect("HRM.db") as conn:
        if request.method == 'POST':
            username = request.form['username']
            userid = request.form['userid']
            mailid = request.form['mail']
            password = request.form['password']
            hashed_pass = hashlib.md5(password.encode())
            hashed_pass = hashed_pass.hexdigest()
            cursors = conn.cursor()

            insert_into_HR_table = """INSERT INTO HR (userid,username,mailID,password) VALUES (?,?,?,?);"""
            data_tuple  =(userid,username,mailid,hashed_pass)
            cursors.execute(insert_into_HR_table, data_tuple)
            conn.commit()
        return render_template('signup.html')

#Login page for admins.
@app.route('/login/')
def loginPageForHRs():
    return render_template('login.html')

#Admin login is autheticated and directed further in the below route.
@app.route('/loginasHR/',methods=['POST'])
def loginasHR():
    with sqlite3.connect("HRM.db") as con:
        if request.method == 'POST':            
            userid = request.form['userid']
            session['username'] = userid
            pwd = request.form['password']
            validate_pass = hashlib.md5(pwd.encode())
            validate_pass = validate_pass.hexdigest()

            c = con.execute("SELECT * from HR where userid=(?)",(userid,))
            for row in c:
                if(row[3] == validate_pass):
                    return render_template('welcome.html',userid_flag=userid)
                else:
                    error_msg = "The entered user - ID or password is wrong "
                    return render_template('login.html',error_msg=error_msg) 


    render_template('welcome.html')

#Route for adding new employee.
@app.route('/addEmp/')
def addNewEmployee():
    return render_template('addEmp.html',userid_flag=session['username'])

#Adding employee and inserting in DB happens here.
@app.route('/createemp/',methods=['POST'])
def createemployee():
    with sqlite3.connect("HRM.db") as don:
        if request.method == 'POST':
            eid = request.form['empid']
            ename = request.form['empname']
            eaddr = request.form['address']
            email = request.form['mailID']
            eage = request.form['age']
            ephone = request.form['phone']
            edesig = request.form['designation']
            maxsal = 0

            if(edesig == "Team leader"):
                maxsal=75000
            elif(edesig == "UI/UX engineer"):
                maxsal=55000
            elif(edesig == "Backend developer"):
                maxsal = 65000
            elif(edesig == "Frontend developer"):
                maxsal = 60000
            elif(edesig == "Devops engineer"):
                maxsal = 50000
            cursorda = don.cursor()


            insert_into_EMP_table = """INSERT INTO EMPLOYEE (emp_id,emp_name,emp_age,mailID,address,phonenumber,designation,max_sal) VALUES (?,?,?,?,?,?,?,?);"""
            d_t_1 = (eid,ename,eage,email,eaddr,ephone,edesig,maxsal)
            cursorda.execute(insert_into_EMP_table,d_t_1)
            don.commit()

        return render_template('addEmp.html',userid_flag=session['username'])


#The below route will throw a list of employees to select and update a particular employee. 
@app.route('/updateEmp/')
def updateEmpPageThrower():
    with sqlite3.connect("HRM.db") as honey:
        employeeID = []
        employeeName = []
        to_list_emp = honey.execute('SELECT emp_id,emp_name FROM EMPLOYEE')
        for row in to_list_emp:
            employeeID.append(row[0])
            employeeName.append(row[1])

        request_data = {'userid_flag':session['username'],'eid':employeeID,'ename':employeeName,'eidlen':len(employeeID)}       

        return render_template('updateEmp.html',**request_data)

#A selected employee's details are made ready for updation as a form.
@app.route('/updateEmpID/<string:Emp_ID>')
def updateEmpID(Emp_ID):
    with sqlite3.connect("HRM.db") as caramel:
        to_get_empid = str(Emp_ID)
        e_q_2 = caramel.execute("SELECT * FROM EMPLOYEE WHERE emp_id=(?)",(to_get_empid,))
        for row in e_q_2:
            update_emp_id = row[0]
            update_emp_name = row[1]
            update_emp_age = row[2]
            update_mailID = row[3]
            update_address=row[4]
            update_phone = row[5]
            update_designation = row[6]
            update_maxsal = row[7]

        to_update_emp_details = {'empid':update_emp_id,'empname':update_emp_name,
        'empage':update_emp_age,'empmail':update_mailID,'empaddress':update_address,
        'empphone':update_phone,'empdes':update_designation,'empsal':update_maxsal,'userid_flag':session['username']}

        return render_template('empUpdationForm.html',**to_update_emp_details)

# Actual updation of an employee happens here and updated in DB.
@app.route('/aue/',methods=['POST'])
def actualEmployeeUpdationHappensHere():
    with sqlite3.connect("HRM.db") as jamun:
        if request.method == 'POST':
            ueid = request.form['empid']
            uename = request.form['empname']
            uaddress = request.form['address']
            umail = request.form['mailID']
            uage = request.form['age']
            uphone = request.form['phone']
            udesig = request.form['designation']

            umaxsal = 0

            if(udesig == "Team leader"):
                umaxsal=75000
            elif(udesig == "UI/UX engineer"):
                umaxsal=55000
            elif(udesig == "Backend developer"):
                umaxsal = 65000
            elif(udesig == "Frontend developer"):
                umaxsal = 60000
            elif(udesig == "Devops engineer"):
                umaxsal = 50000

            cursordooi = jamun.cursor()

            update_into_emp_table = """UPDATE EMPLOYEE SET emp_name=?,emp_age=?,mailID=?,address=?,phonenumber=?,designation=?,max_sal=? WHERE emp_id=?"""
            cursordooi.execute(update_into_emp_table,(uename,uage,umail,uaddress,uphone,udesig,umaxsal,ueid,))
            jamun.commit()

        return redirect(url_for('updateEmpPageThrower'))

@app.route('/salaryCalc/')
def salaryFileHandling():
    return render_template('fileUpload.html',userid_flag=session['username'])

@app.route('/csvHandle/',methods=['POST'])
def csvFileHandler():
    with sqlite3.connect("HRM.db") as juice:
        if request.method == 'POST':
            f = request.files['file']
            # print(str(f.filename))
            f.save(secure_filename(f.filename))
            month = request.form['month']
            year = request.form['year']
            fname = str(f.filename)
            pay_dict = {}
            with open(fname) as csv_file:
                csv_reader = csv.reader(csv_file,delimiter=',')
                linecount = 0
                a=0
                for row in csv_reader:
                    if linecount == 0: 
                        a=1
                        linecount = 1
                    else:            
                        if(row[0] not in pay_dict):             
                            pay_dict[row[0]] = {'empid':row[0],'present':0,'absent':0}
                            if row[2] == 'P':
                                pay_dict[row[0]]['present'] +=1
                            elif row[2] == 'A':
                                pay_dict[row[0]]['absent'] +=1

                        else:
                            if row[2] == 'P':
                                pay_dict[row[0]]['present'] += 1    
                            elif row[2] == 'A':
                                pay_dict[row[0]]['absent'] += 1

            all_emp_details = juice.execute('SELECT * FROM EMPLOYEE')
            for r in all_emp_details:
                pay_dict[r[0]]['name'] = r[1]
                pay_dict[r[0]]['email'] = r[3]                
                pay_dict[r[0]]['maxsal'] = r[7]
                maximumsSal = pay_dict[r[0]]['maxsal']
                pay_dict[r[0]]['netsal'] = int(maximumsSal) - ( (int(maximumsSal)/31) * abs( int(pay_dict[r[0]]['absent']) - 5) )
                pay_dict[r[0]]['month'] = month
                pay_dict[r[0]]['year'] = year
                
                s = smtplib.SMTP('smtp.gmail.com',587)
                s.starttls()
                s.login("hercules.office96@gmail.com","godofstrength@96")
                message = """Hello {name},
                Your {month},{year}  salary details are :
                No. of days present : {present}
                No. of days absent  : {absent}
                Net salary          : {salary}

                Regards,
                Hercules management.
                """.format(name = pay_dict[r[0]]['name'],month=month,year=year,present=pay_dict[r[0]]['present'],absent=pay_dict[r[0]]['absent'],salary=round(pay_dict[r[0]]['netsal'],2) )
                sender = "hercules.office96@gmail.com"
                to = pay_dict[r[0]]['email']
                s.sendmail(sender,to,message)
                s.quit()

            data_to_use = {'userid_flag':session['username'],'status':"Successfully mailed to all the employees."}
            return render_template('fileUpload.html',**data_to_use)



#Logout route will end the session for the current admin and goes to homepage.
@app.route('/logout/')
def logout():
    session.pop('username',None)
    return redirect(url_for('homepage'))
