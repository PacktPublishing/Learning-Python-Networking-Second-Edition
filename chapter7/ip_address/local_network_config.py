#!/usr/bin/env python3

import socket
import netifaces

# Find host info
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: {0}".format(host_name))

# Get interfaces list
ifaces = netifaces.interfaces()

for iface in ifaces:
	ipaddrs = netifaces.ifaddresses(iface)
	#for each ipaddress
	if netifaces.AF_INET in ipaddrs:
		ipaddr_desc = ipaddrs[netifaces.AF_INET]
		ipaddr_desc = ipaddr_desc[0]
		print("Network interface: {0}".format(iface))
		if 'addr' in ipaddr_desc:
			print("\tIP address: {0}".format(ipaddr_desc['addr']))
		if 'netmask' in ipaddr_desc:
			print("\tNetmask: {0}".format(ipaddr_desc['netmask']))

# Find the gateway
gateways = netifaces.gateways()
print("Default gateway:{0}".format(gateways['default'][netifaces.AF_INET][0]))