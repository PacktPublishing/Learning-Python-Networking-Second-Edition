#!/usr/bin/env python3

from lxml.html import fromstring, tostring
from lxml.html import parse, submit_form

import requests
response = requests.get('https://duckduckgo.com')
form_page = fromstring(response.text)
form = form_page.forms[0]
print(tostring(form))

page = parse('http://duckduckgo.com').getroot()
page.forms[0].fields['q'] = 'python'
result = parse(submit_form(page.forms[0])).getroot()
print(tostring(result))