#!/usr/bin/env python3

import sys, requests

try:
	rfc_number = int(sys.argv[1])

except (IndexError, ValueError):
	print('Must supply an RFC number as first argument')
	sys.exit(2)

template = 'https://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc = requests.get(url).text
print(rfc)