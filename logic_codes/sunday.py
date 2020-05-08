import calendar
from datetime import datetime

year = 2020
month = 3
day_to_count = calendar.SUNDAY

matrix = calendar.monthcalendar(year,month)
num_days = sum(1 for x in matrix if x[day_to_count] != 0)
print(num_days)