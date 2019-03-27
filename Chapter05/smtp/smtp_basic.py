#!/usr/bin/env python3

import smtplib

smtp = smtplib.SMTP('smtp_server')

try:
    smtp.sendmail('from@fromdomain.com', ['to@todomain.com'], "This is a test e-mail message")
except SMTPException as exception:
    print("Error: unable to send email: "+exception)
finally:
    smtp.quit()
