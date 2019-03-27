#!/usr/bin/env python3

from lxml.html import fromstring
import requests

domain = input("Enter the domain : ")
url = 'http://whois.domaintools.com/' + domain
headers = {'User-Agent': 'wswp'}
resp = requests.get(url, headers=headers)
html = resp.text

tree = fromstring(html)
info = tree.xpath('//*[@id="stats"]//table/tbody/tr//text()')

temp_list = []
for each in info:
    each = each.strip()
    if each == "":
        continue
    temp_list.append(each.strip("\n"))

ip_index = temp_list.index('IP Address')
print("IP address ", temp_list[ip_index + 1])

location = temp_list.index('IP Location')
location2 = temp_list.index('ASN')
print('Location : ', "".join(temp_list[location + 1:location2]))
