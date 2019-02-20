#!/usr/bin/env python3

import socket,sys

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT = 12345
buffer=4096

socket_server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #UDP
socket_server.bind((UDP_IP_ADDRESS,UDP_PORT))

while True:
	print("Waiting for client...")
	data,address = socket_server.recvfrom(buffer)
	data = data.strip()
	print("Data Received from address: ",address)
	print("message: ", data)
		
	try:
		response = "Hi %s" % sys.platform
	except Exception as e:
		response = "%s" % sys.exc_info()[0]
	
	print("Response",response)
	
	socket_server.sendto(response.encode(),address)
		
socket_server.close()
		
