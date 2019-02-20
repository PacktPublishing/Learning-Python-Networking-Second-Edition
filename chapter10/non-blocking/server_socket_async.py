#!/usr/bin/env python3

import socket

if __name__ == '__main__':
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	#unset blocking
	sock.setblocking(0)
	sock.settimeout(0.5)
	sock.bind(("127.0.0.1", 12345))
	socket_address =sock.getsockname()
	print("Asynchronous socket server launched on socket: %s" %str(socket_address))
	while(1):
		sock.listen(1)