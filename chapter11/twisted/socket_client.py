#!/usr/bin/env python3

from socket import socket

s = socket()
s.connect(("127.0.0.1", 8080))

while True:
    output_data = input("Enter message> ")
    if output_data:
        s.send(output_data.encode())
        input_data = s.recv(1024)
        if input_data:
            print(input_data.decode("utf-8"))