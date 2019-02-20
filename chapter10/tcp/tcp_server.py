#!/usr/bin/env python3

import socket

host = '127.0.0.1'
port = 12345
BUFFER_SIZE = 1024

#The socket objects support the context manager type
#so we can use it with a with statement, there's no need to call socket_close ()

# We create a TCP type socket object
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.bind((host, port))
	# We wait for the client connection
    socket_tcp.listen(5)
	# We establish the connection with the client
    connection, addr = socket_tcp.accept()
    with connection:
        print('[*] Established connection') 
        while True:
            # We receive bytes, we convert into str
            data = connection.recv(BUFFER_SIZE)
            # We verify that we have received data
            if not data:
                break
            else:
                print('[*] Data received: {}'.format(data.decode('utf-8'))) 
            connection.send(data)