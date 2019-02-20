#!/usr/bin/env python3

import socket

if __name__ == '__main__':
	
	sock = socket.socket()
	
	sock.connect(("127.0.0.1", 12345))
	
	#setting to non-blocking mode
	sock.setblocking(0)
	
	data = "Hello Python"
	sock.send(data.encode())