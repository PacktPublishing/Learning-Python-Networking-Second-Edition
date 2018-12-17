#!/usr/bin/env python3

import requests

data_dictionary = {'custname': 'customer','custtel': '323232',
'size': 'large','custemail': 'email@domain.com'}
response = requests.post("http://httpbin.org/post",data=data_dictionary)

# we then print out the http status_code
print("HTTP Status Code: " + str(response.status_code))

if response.status_code == 200:
	print(response.text)
