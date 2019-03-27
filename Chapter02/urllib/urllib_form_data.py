#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.request import Request
import json

data_dict = {'custname': 'customer','custtel': '323232',
'size': 'large','custemail': 'email@domain.com'}
data = urlencode(data_dict).encode('utf-8')
print(data)

req = Request('http://httpbin.org/post',data=data)
req.add_header('Content-Type', 'application/x-www-form-urlencode;charset=UTF-8')

response = urlopen(req)
response_dictionary = json.load(response)
print(response_dictionary)