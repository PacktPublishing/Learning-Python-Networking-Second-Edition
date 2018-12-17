#!/usr/bin/env python3

import urllib3

pool = urllib3.PoolManager(10)

PROXY_ADDRESS = "http://165.24.10.8:8080"

proxy = urllib3.ProxyManager(PROXY_ADDRESS)

response = proxy.request('GET','http://www.packtpub.com')
print(response.status)
response.headers.keys()
response.headers.values()
for header,value in response.headers.items():
	print(header + ":" + value)