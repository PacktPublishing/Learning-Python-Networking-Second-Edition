#!/usr/bin/env python3

import urllib.error

from urllib.request import urlopen

try:
	urlopen('https://www.ietf.org/rfc/rfc0.txt')
	
except urllib.error.HTTPError as e:
	print('Exception', e)
	print('status', e.code)
	print('reason', e.reason)
	print('url', e.url)