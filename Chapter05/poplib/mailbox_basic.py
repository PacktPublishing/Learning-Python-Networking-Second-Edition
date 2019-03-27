#!/usr/bin/env python3

import poplib

mailbox = poplib.POP3_SSL("pop.gmail.com",995)
mailbox.user("user")
mailbox.pass_("password")

print(mailbox.getwelcome())

messages = len(mailbox.list()[1])

for index in range(messages):
    for message in mailbox.retr(index+1)[1]:
        print(message)
 
mailbox.quit()

