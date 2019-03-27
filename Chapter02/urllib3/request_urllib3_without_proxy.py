#!/usr/bin/env python3

import urllib3

pool = urllib3.PoolManager(10)
response = pool.request('GET','http://www.packtpub.com')
print(response.status)
response.headers.keys()
response.headers.values()
for header,value in response.headers.items():
	print(header + ":" + value)