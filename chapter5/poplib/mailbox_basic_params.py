#!/usr/bin/env python3

import poplib, sys

if len(sys.argv) != 4:
    print('usage: %s hostname port user password' % sys.argv[0])
    exit(2)

hostname, port , user, password = sys.argv[1:]

mailbox = poplib.POP3_SSL(hostname,port)

try:
    mailbox.user(user)
    mailbox.pass_(password)
except poplib.error_proto as exception:
    print("Login failed:", exception)
else:
    response, listings, octet_count = mailbox.list()
    for listing in listings:
        number, size = listing.decode('ascii').split()
        print("Message %s has %s bytes" % (number, size))
finally:
    mailbox.quit()
