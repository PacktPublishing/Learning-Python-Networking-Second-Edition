#!/usr/bin/env python3

import socket
import psutil

def get_ip_addresses(family):
    for interface, snics in psutil.net_if_addrs().items():
        for snic in snics:
            if snic.family == family:
                yield (interface, snic.address)

if __name__ == '__main__':
	ipv4_list = list(get_ip_addresses(socket.AF_INET))
	ipv6_list = list(get_ip_addresses(socket.AF_INET6))
	print("IPV4 Interfaces",ipv4_list)
	print("IPV6 Interfaces",ipv6_list)
