#!/usr/bin/env python3

import socket
import netifaces
import netaddr

def extract_ipv6_info():
    print ("IPv6 support built into Python: %s" %socket.has_ipv6)
    for interface in netifaces.interfaces():
        all_addresses = netifaces.ifaddresses(interface)
        print ("Interface %s:" %interface)
        for family,addrs in all_addresses.items():
            fam_name = netifaces.address_families[family]

            for addr in addrs:
                if fam_name == 'AF_INET6':
                    addr = addr['addr']
                    has_eth_string = addr.split("%eth")
                    if has_eth_string:
                        addr = addr.split("%eth")[0]
                    try:
                        print ("    IP Address: %s" %netaddr.IPNetwork(addr))
                        print ("    IP Version: %s" %netaddr.IPNetwork(addr).version)
                        print ("    IP Prefix length: %s" %netaddr.IPNetwork(addr).prefixlen)
                        print ("    Network: %s" %netaddr.IPNetwork(addr).network)
                        print ("    Broadcast: %s" %netaddr.IPNetwork(addr).broadcast)
                    except Exception as e:
                        print ("Skip Non-IPv6 Interface")

if __name__ == '__main__':
    extract_ipv6_info()
