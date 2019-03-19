#!/usr/bin/env python3

import sys
from imapclient import IMAPClient

import getpass

username = input('Enter your username:')
password = getpass.getpass(prompt='Enter your password:')

server = IMAPClient('imap.gmail.com', ssl=True)

try:
    server.login(username, password)
except server.Error as e:
    print('Could not log in:', e)
    sys.exit(1)

print('Capabilities:', server.capabilities())
print('Listing mailboxes:')
data = server.list_folders()
for flags, delimiter, folder_name in data:
    print('  %-30s%s %s' % (' '.join(str(flags)), delimiter, folder_name))
	
server.logout()
