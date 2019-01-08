#!/usr/bin/env python3

from imapclient import IMAPClient

server = IMAPClient('imap.gmail.com', ssl=True)
server.login('user', 'password')
select_info = server.select_folder('INBOX',readonly=True)

for k, v in list(select_info.items()):
	print('%s: %r' % (k, v))
	
server.logout()

