# import yagmail
# yagmail.register('hercules.office96@gmail.com','godofstrength@96')
# yag = yagmail.SMTP('hercules.office96@gmail.com')
import smtplib
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("hercules.office96@gmail.com","godofstrength@96")


# subject = "{month}, {year} salary details.".format(month='March',year='2020')
message = """Hello {name},
             Your {month},{year}  salary details are :
             No. of days present : {present}
             No. of days absent  : {absent}
             Net salary          : {salary}

             Regards,
             Hercules management.
""".format(name = 'Jim Halpert',month='March',year='2020',present='24',absent='7',salary='71042.59')

sender = "hercules.office96@gmail.com"
to = "thejaspalani@gmail.com"
s.sendmail(sender,to,message)
s.quit()