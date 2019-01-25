#!/usr/bin/env python3

import ipaddress as ip

CLASS_C_ADDR = '192.168.0.0'

mask = input("Enter the mask len (24-30): ")
mask = int(mask)
if mask not in range(23, 31):
	raise Exception("Mask length must be between 24 and 30")

net_addr = CLASS_C_ADDR + '/' + str(mask)
print("Using network address:%s " %net_addr)

try:
	network = ip.ip_network(net_addr)
except:
	raise Exception("Failed to create network object")

print("This mask will give %s IP addresses" %(network.num_addresses))
print("The network configuration will be:")
print("\t network address: %s" %str(network.network_address))
print("\t netmask: %s" %str(network.netmask))
print("\t broadcast address: %s" %str(network.broadcast_address))
first_ip, last_ip = list(network.hosts())[0], list(network.hosts())[-1]
print("\t host IP addresses: from %s to %s" %(first_ip,last_ip))