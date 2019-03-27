#!/usr/bin/env python3

import ipaddress as ip

IPV6_ADDR = '2001:db8:0:1::'

mask = input("Enter the mask lengh: ")
mask = int(mask)
net_addr = IPV6_ADDR + '/' + str(mask)

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