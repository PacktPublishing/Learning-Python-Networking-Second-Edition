#!/usr/bin/env python3

import socket

def getaddrinfoIPv4(host, port=80, family=0, type=0, proto=0, flags=0):
    return socket.getaddrinfo(host=host, port=port, 
		family=socket.AF_INET, type=type, proto=proto, flags=flags) 
		
def getaddrinfoIPv6(host, port=80, family=0, type=0, proto=0, flags=0):
    return socket.getaddrinfo(host=host, port=port, 
		family=socket.AF_INET6, type=type, proto=proto, flags=flags) 


print(getaddrinfoIPv4("www.python.org"))

print(getaddrinfoIPv6("www.python.org"))
