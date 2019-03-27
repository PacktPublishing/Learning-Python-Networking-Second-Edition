#!/usr/bin/env python3

import dns.resolver
answers = dns.resolver.query('dnspython.org', 'A')
for rdata in answers:
	print('IP', rdata.to_text())


