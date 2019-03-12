#!/usr/bin/env python3

import socket

ipaddress =input("Enter ip address or domain for port scanning:")

port_init= input("Enter first port: ")
port_end = input("Enter last port:  ")

for port in range(int(port_init), int(port_end)+1):
	sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	sock.settimeout(5)
	result = sock.connect_ex((ipaddress,port))
	if result == 0:
		print(port, "--> Open")
	else:
		print(port, "--> Closed")
	sock.close()

