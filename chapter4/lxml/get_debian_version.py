#!/usr/bin/env python3

import re
import requests

from lxml.etree import HTML
response = requests.get('https://www.debian.org/releases/stable/index.en.html')
root = HTML(response.content)

title_text = root.find('head').find('title').text
release = re.search('\u201c(.*)\u201d', title_text).group(1)
p_text = root.xpath('//div[@id="content"]/p[1]')[0].text
version = p_text.split()[1]

print('Codename: {}\nVersion: {}'.format(release, version))