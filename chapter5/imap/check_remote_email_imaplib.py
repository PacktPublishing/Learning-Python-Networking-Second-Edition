#!/usr/bin/env python3

import argparse
import getpass
import imaplib

GMAIL_IMAP_SERVER = 'imap.gmail.com'

def check_email(username,password): 
    mailbox = imaplib.IMAP4_SSL(GMAIL_IMAP_SERVER, '993')
    mailbox.login(username, password)
    mailbox.select('Inbox')
    typ, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        typ, data = mailbox.fetch(num, '(RFC822)')
        print ('Message %s\n%s\n' % (num, data[0][1]))
        break
    mailbox.close()
    mailbox.logout()
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Email Download IMAP')
    parser.add_argument('--username', action="store", dest="username", default=getpass.getuser())
    given_args = parser.parse_args() 
    username = given_args.username
    password = getpass.getpass(prompt="Enter you account password:")
	check_email(username, password)

