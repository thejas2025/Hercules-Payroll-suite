import pandas as pd
import numpy as np

data = pd.read_csv('E:/Amrita University/Academics/3rd year 2019-20/6th Semester/Open Labs/Project/Employee_payroll_flask/dataset/March_2020.csv')

att_emp = data.groupby('Attendance')['Emp_id'].value_counts()

present = att_emp['P']
absent = att_emp['A']

print(present)
print(absent)

