#!/usr/bin/env python3

import requests

cookies = []
url = 'http://httpbin.org/cookies'

cookies = dict(admin='True')
cookie_req = requests.get(url, cookies=cookies)
print(cookie_req.text)
