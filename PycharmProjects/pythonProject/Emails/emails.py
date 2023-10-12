import getpass
import smtplib

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
print(smtp_object.ehlo())
print(smtp_object.starttls())
# password1 = input('Enter the password')
# password2 = getpass.getpass('password please')
email = getpass.getpass("email:")
password = getpass.getpass("password:")
smtp_object.login(email, password)

from_address = email
to_address = email
subject = input("Enter the subject line:")
message = input("Enter the body message ")
msg = "subject: "+subject+'\n'+message

smtp_object.sendmail(from_address,to_address,msg)
