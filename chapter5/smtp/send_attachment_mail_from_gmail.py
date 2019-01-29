#!/usr/bin/env python3

from email.mime.multipart import MIMEMultipart
from email.MIMEImage import MIMEImage
from email.mime.text import MIMEText
import smtplib
 
# create message object instance
message = MIMEMultipart()
 
 # setup the parameters of the message
message['From'] = "user@domain"
message['To'] = "user@domain"
message['Subject'] = "sending images as attachment"
 
# attach image to message body
message.attach(MIMEImage(file("image.jpg").read()))

# create server
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()

# Login Credentials for sending the mail
server.login(message['From'], "password")

# send the message via the server.
server.sendmail(message['From'], message['To'], message.as_string())
server.quit()
print "successfully sent email to %s:" % (message['To'])
