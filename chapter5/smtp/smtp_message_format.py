#!/usr/bin/env python3

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = 'sender@domain.com'
receiver = 'receiver@domain.com'

mail_host="smtp.domain.com"
mail_user="user"  
mail_password="password"

message = MIMEText('Python', 'plain', 'utf-8')
message['From'] = Header(sender, 'utf-8')
message['To'] =  Header(receiver, 'utf-8')

subject = 'Python SMTP'
message['Subject'] = Header(subject, 'utf-8')

smtp = smtplib.SMTP()

try:
	smtp.connect(mail_host, 25)
	smtp.login(mail_user,mail_password)
	smtp.sendmail(sender, receiver, message.as_string())
except smtplib.SMTPException as exception:
	print("Error:"+exception)
finally:
	smtp.quit()
