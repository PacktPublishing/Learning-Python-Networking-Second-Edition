#!/usr/bin/env python3

import argparse 
import socket

IPV6_ADDRESS = '::1'
# Up to 5 clients can connect
maxConnections = 5

def echo_server_ipv6(port, host=IPV6_ADDRESS):
	
	# Creating the server with ipv6 support
	# socket.AF_INET6 to indicate that we will use Ipv6
	# socket.SOCK_STREAM to use TCP/IP
	try:
		server_socket = socket.socket(socket.AF_INET6,socket.SOCK_STREAM)
		dataConection = (host,port)
		server_socket.bind(dataConection)
		
		# We assign the maximum number of connections
		server_socket.listen(maxConnections)
	except socket.error as err:
		print ("Socket error: %s" %err)
		server_socket.close()
	
	print("Waiting connections in %s:%s" %(host, port))
	connection, address = server_socket.accept()
	print ('Connected to', address)
	
	while True:
		data = connection.recv(1024)
		print ("Received data from the client: [%s]" %data.decode())
		if data.decode() == "exit":
			connection.send(bytes("exit".encode('utf-8')))
			break
		connection.send(data)
		print ("Sent data echoed back to the client: [%s]" %data.decode())
		
	print("------- CLOSE CONNECTION ---------")
	connection.close()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='IPv6 Socket Server')
	parser.add_argument('--port', action="store", dest="port", type=int, required=True)
	given_args = parser.parse_args()
	port = given_args.port
	echo_server_ipv6(port)
    
