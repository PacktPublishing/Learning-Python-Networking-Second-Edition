#!/usr/bin/env python3

import argparse
import imaplib

def check_email(username,password): 
    mailbox = imaplib.IMAP4_SSL('imap.gmail.com', '993')
    mailbox.login(username, password)
    mailbox.select('Inbox')
    type, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        type, data = mailbox.fetch(num, '(RFC822)')
        print ('Message %s\n%s\n' % (num, data[0][1]))
    mailbox.close()
    mailbox.logout()
    

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Email Download IMAP')
	parser.add_argument('--username', action="store", dest="username")
	parser.add_argument('--password', action="store", dest="password")
	given_args = parser.parse_args()
	username = given_args.username
	password = given_args.password
	check_email(username, password)

