#!/usr/bin/env python3

import socket
import netifaces

def inspect_ipv6_support():
    print ("IPV6 support built into Python: %s" %socket.has_ipv6)
    ipv6_addresses = {}
    for interface in netifaces.interfaces():
        all_addresses = netifaces.ifaddresses(interface)
        print ("Interface %s:" %interface)
        for family,addrs in all_addresses.items():
            fam_name = netifaces.address_families[family]
            print ('  Address family: %s' % fam_name)
            for addr in addrs:
                if fam_name == 'AF_INET6':
                    ipv6_addresses[interface] = addr['addr']
                print ('    Address  : %s' % addr['addr'])
                nmask = addr.get('netmask', None)
                if nmask:
                    print ('    Netmask  : %s' % nmask)
                bcast = addr.get('broadcast', None)
                if bcast:
                    print ('    Broadcast: %s' % bcast)
    if ipv6_addresses:
        print ("Found IPv6 address: %s" %ipv6_addresses)
    else:
        print ("No IPv6 interface found!")  

   
if __name__ == '__main__':
    inspect_ipv6_support()
