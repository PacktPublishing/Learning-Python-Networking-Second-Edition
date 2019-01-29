#!/usr/bin/env python3

import sys, smtplib, socket

# this invokes the secure SMTP protocol (port 465, uses SSL)
from smtplib import SMTP_SSL as SMTP   
from email.mime.text import MIMEText 

try:
	msg = MIMEText("Test message", 'plain')
	msg['Subject']=  "Sent from Python"
	msg['From'] = 'user@gmail.com'
	
	#smtp = SMTP()
	#smtp.connect("smtp.gmail.com",587)
	
	# create smtp session
	smtp = smtplib.SMTP("smtp.gmail.com", 587)
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
		smtp.login("user@gmail.com", "password")
	except smtplib.SMTPException as e:
		print("Authentication failed:", e)
		sys.exit(1)

	try:
		smtp.sendmail('user@gmail.com', ['user@gmail.com'], msg.as_string())
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