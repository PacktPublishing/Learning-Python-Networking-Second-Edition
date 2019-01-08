#!/usr/bin/env python3

import poplib

mailbox = poplib.POP3_SSL("pop.gmail.com",995)

user="user"
password="password"

mailbox.user(user)
mailbox.pass_(password)

print(mailbox.getwelcome())

numMessages = len(mailbox.list()[1])

for i in range(numMessages):
    for msg in mailbox.retr(i+1)[1]:
        print(msg)
		
mailbox.quit()

