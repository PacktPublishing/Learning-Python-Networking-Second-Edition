#!/usr/bin/env python3

import requests
import re
from bs4 import BeautifulSoup

url = input("Enter the URL: ")
response = requests.get(url)
html_page = response.text
email_pattern=re.compile(r'\b[\w.-]+?@\w+?\.\w+?\b')

for match in re.findall(email_pattern,html_page):
	print(match)

