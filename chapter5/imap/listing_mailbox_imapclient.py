#!/usr/bin/env python3

import sys
from imapclient import IMAPClient

server = IMAPClient('imap.gmail.com', ssl=True)

try:
    server.login('user', 'password')
except server.Error as e:
    print('Could not log in:', e)
    sys.exit(1)

print('Capabilities:', server.capabilities())
print('Listing mailboxes:')
data = server.list_folders()
for flags, delimiter, folder_name in data:
    print('  %-30s%s %s' % (' '.join(flags), delimiter, folder_name))
	
server.logout()
