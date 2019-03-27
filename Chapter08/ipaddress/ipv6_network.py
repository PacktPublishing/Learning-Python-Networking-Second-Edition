#!/usr/bin/env python3

import ipaddress

net6 = ipaddress.ip_network('12:3456:78:90ab:cd:ef01:23:30/125')
for ip in net6:
	print(ip)