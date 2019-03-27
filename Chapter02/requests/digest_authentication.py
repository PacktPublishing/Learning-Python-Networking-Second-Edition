#!/usr/bin/env python3

import requests
from requests.auth import HTTPDigestAuth

url = 'http://httpbin.org/digest-auth/auth/user/pass'
response = requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
print('Response.status_code:'+ str(response.status_code))
if response.status_code == 200:
	print('Login successful :'+str(response.json()))