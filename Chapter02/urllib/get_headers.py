#!/usr/bin/env python3

import urllib.request

url = input("Enter the URL:")

http_response = urllib.request.urlopen(url)

if http_response.code == 200:
	print(http_response.headers)
	for key,value in http_response.getheaders():
		print(key,value)
	