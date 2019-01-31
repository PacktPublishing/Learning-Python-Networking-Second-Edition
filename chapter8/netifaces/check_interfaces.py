#!/usr/bin/env python3

import itertools
from netifaces import interfaces, ifaddresses, AF_INET, AF_INET6

def all_interfaces():
	for interface in interfaces():
		print(ifaddresses(interface))

def inspect_ipv4_addresses():
	links = filter(None, (ifaddresses(x).get(AF_INET) for x in interfaces()))
	links = itertools.chain(*links)
	ip_v4_addresses = [x['addr'] for x in links]
	return ip_v4_addresses
	
def inspect_ipv6_addresses():
	links = filter(None, (ifaddresses(x).get(AF_INET6) for x in interfaces()))
	links = itertools.chain(*links)
	ip_v6_addresses = [x['addr'] for x in links]
	return ip_v6_addresses
	
if __name__ == '__main__':
	print(inspect_ipv4_addresses())
	print(inspect_ipv6_addresses())
	all_interfaces()

