#!/usr/bin/python3

import socket
import re

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.packtpub.com", 80))

http_get = b"GET / HTTP/1.1\nHost: www.packtpub.com\n\n"
data = ''
try:
	sock.sendall(http_get)
	data = sock.recvfrom(1024)
	strdata = data[0]
	headers = strdata.splitlines()
	for header in headers:
		print(header.decode())
except socket.error:
	print ("Socket error", socket.errno)
finally:
	print("closing connection")
	sock.close()


