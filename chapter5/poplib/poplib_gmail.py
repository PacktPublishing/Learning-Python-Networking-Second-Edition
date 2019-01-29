#!/usr/bin/env python3

import poplib

mailbox = poplib.POP3_SSL ('pop.gmail.com', 995)
mailbox.user('user@gmail.com')
mailbox.pass_('password')

EmailInformation = mailbox.stat()
print("Number of new emails: %s ", EmailInformation)
numberOfMails = EmailInformation[0]

num_messages = len(mailbox.list()[1])

for i in range (num_messages):
   print("Message number "+str(i+1))
   print("--------------------")
   # read message
   response, headerLines, bytes = mailbox.retr(i+1)
   message = '\n'.join (headerLines)
   #Parsing the message
   parser = Parser()
   email = p.parsestr(message)
   print("From: "+email["From"])
   print("To: "+email["To"])
   print("Subject: "+email["Subject"])
   print("ID: "+email['message-id'])
   content_type = email.get_content_type()
   if ("text/plain" == str(content_type)):
      print(email.get_payload(decode=True))
   # If it is an image, the name of the file is extracted
   elif ("image/gif" == str(content_type)):
      file_name = email.get_filename()
      fp = open(file_name, 'wb')
      fp.write(part.get_payload(decode = True))
      fp.close()

mailbox.quit()

   
