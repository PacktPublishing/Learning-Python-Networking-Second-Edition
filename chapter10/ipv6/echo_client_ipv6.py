#!/usr/bin/env python3

import argparse
import socket

IPV6_ADDRESS = '::1'

def echo_client_ipv6(port, host=IPV6_ADDRESS):
	
	# Configure the data to connect to the server
	# socket.AF_INET6 to indicate that we will use Ipv6
	# socket.SOCK_STREAM to use TCP/IP
	# These protocols must be the same as on the server
	try:
		client = socket.socket (socket.AF_INET6, socket.SOCK_STREAM)
		client.connect ((host, port))
		print ("Connected to the server --->% s:% s"% (host, port))
	except socket.error as err:
		print ("Socket error:%s" %err)
		client.close()
	
    # send initial data to server
	message = "Hello from ipv6 client"
	print ("Send data to server: %s" %message)
	client.send(bytes(message.encode('utf-8')))
	data = client.recv(4096)
	print ('Received initial message from server:', data.decode())
	
	while True:
		message = input("Write your message > ")
		client.send(bytes(message.encode('utf-8')))
		data = client.recv(4096)
		print ('Received from server:', data.decode())
		if data.decode() == "exit":
			break;
		command = input("Write your command > ")
		command = "command/"+command
		client.send(bytes(command.encode('utf-8')))
		data = client.recv(4096)
		print ('Received command server:', data.decode())
		
	print("------- CLOSE CONNECTION ---------")
	client.close()
    
if __name__ == '__main__': 
	parser = argparse.ArgumentParser(description='IPv6 socket client')
	parser.add_argument('--port', action="store", dest="port", type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_client_ipv6(port)
