#!/usr/bin/env python3

import poplib
import getpass

mailbox = poplib.POP3_SSL ('pop.gmail.com', 995)

username = input('Enter your username:')
password = getpass.getpass(prompt='Enter your password:')

mailbox.user(username)
mailbox.pass_(password)

EmailInformation = mailbox.stat()
print("Number of new emails: %s ", EmailInformation)
numberOfMails = EmailInformation[0]

num_messages = len(mailbox.list()[1])

for i in range (num_messages):
   print("\nMessage number "+str(i+1))
   print("--------------------")
   # read message
   response, headerLines, bytes = mailbox.retr(i+1)
   #for header in headerLines:
   #   print(str(header))
   print('Message ID', headerLines[1])
   print('Date', headerLines[2])
   print('Reply To', headerLines[4])
   print('To', headerLines[5])
   print('Subject', headerLines[6])
   print('MIME', headerLines[7])
   print('Content Type', headerLines[8])

mailbox.quit()

   
