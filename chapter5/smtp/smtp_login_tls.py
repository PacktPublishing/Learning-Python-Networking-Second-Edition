#!/usr/bin/env python3

SMTP_SERVER="smtp.gmail.com"
SMTP_PORT = 587
sender =  'user@gmail.com' 
destination = ['user@gmail.com'] 

USERNAME = "user@gmail.com" 
PASSWORD = "password" 

# typical values for text_subtype are plain, html, xml 
text_subtype = 'plain' 
content="Test message"
subject="Sent from Python" 

import sys, smtplib, socket

# this invokes the secure SMTP protocol (port 465, uses SSL)
from smtplib import SMTP_SSL as SMTP   
from email.mime.text import MIMEText 

try:
	msg = MIMEText(content, text_subtype)
	msg['Subject']=  subject
	msg['From'] = sender
	
	#smtp = SMTP()
	#smtp.connect(SMTP_SERVER,SMTP_PORT)
	
	# create smtp session
	smtp = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
	#debug active
	smtp.set_debuglevel(True)
	# identify ourselves to smtp gmail client 
	smtp.ehlo()
	
	# If we can encrypt this session, do it
	if server.has_extn('STARTTLS'):
		# secure our email with tls encryption
		smtp.starttls()
		# re-identify ourselves as an encrypted connection 
		smtp.ehlo()	

	try:
		smtp.login(USERNAME, PASSWORD)
	except smtplib.SMTPException as e:
		print("Authentication failed:", e)
		sys.exit(1)

	try:
		smtp.sendmail(sender, destination, msg.as_string())
	except (socket.gaierror, socket.error, socket.herror,smtplib.SMTPException) as e:
		print(" *** Your message may not have been sent!")
		print(e)
		sys.exit(1)
	finally:
		smtp.quit() 

except (socket.gaierror, socket.error, socket.herror,smtplib.SMTPException) as e:
	print(" *** Your message may not have been sent!")
	print(e)
	sys.exit(1)