#!/usr/bin/env python3

import socket

# The client must have the same server specifications
host = '127.0.0.1'
port = 12345
BUFFER_SIZE = 1024

MESSAGE = 'Hello world,this is my first message' 

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host, port))
    # We convert str to bytes
    socket_tcp.send(MESSAGE.encode('utf-8'))
    data = socket_tcp.recv(BUFFER_SIZE)