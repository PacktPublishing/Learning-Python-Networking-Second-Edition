#!/usr/bin/env python3

import socket

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 12345
buffer=4096

address = (UDP_IP_ADDRESS ,UDP_PORT)

socket_client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	message = input('Enter your message > ')
	if message=="exit":
		break
	socket_client.sendto(message.encode(),address)
	response,addr = socket_client.recvfrom(buffer)
	print("Server response => %s" % response)
		
socket_client.close()
		
