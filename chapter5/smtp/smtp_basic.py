#!/usr/bin/env python3

import smtplib

sender = 'from@fromdomain.com'
receivers = ['to@todomain.com']

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test
This is a test e-mail message.
"""
smtp = smtplib.SMTP('localhost')

try:
	smtp.sendmail(sender, receivers, message)
	print("Successfully sent email")
except SMTPException as exception:
		print("Error: unable to send email: "+exception)
finally:
	smtp.quit()
