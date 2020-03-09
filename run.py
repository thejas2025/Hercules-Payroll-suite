import sqlite3
conn = sqlite3.connect('HRsuite.db')
print("file created")

# conn.execute('''CREATE TABLE HR
#              (userid CHAR(20) PRIMARY KEY NOT NULL,
#              username CHAR(50) NOT NULL,
#              mailID CHAR(50) NOT NULL,
#              password CHAR(100) NOT NULL);''')


# conn.execute('''CREATE TABLE EMPLOYEE
#             ( emp_id CHAR(20) PRIMARY KEY NOT NULL,
#               emp_name CHAR(50) NOT NULL,
#               emp_age INT NOT NULL,
#               mailID CHAR(50) NOT NULL,
#               address CHAR(100) NOT NULL,
#               phonenumber CHAR(10) NOT NULL,
#               designation CHAR(50) NOT NULL,
#               max_sal REAL);''')

# conn.execute('''
#             CREATE TABLE EMPLOYEE_ATTENDANCE
#             ( emp_id CHAR(20) NOT NULL,
#               month_year CHAR(10),
#               attendance_count INT,
#               leave_count INT);''')


# conn.execute('''
#             CREATE TABLE SALARY
#             (
#              emp_id CHAR(20) NOT NULL,
#              month_year CHAR(10),
#              calc_sal REAL   
#             );''')



conn.commit()



print("Table created successfully")
