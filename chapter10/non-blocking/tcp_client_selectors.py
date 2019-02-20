#!/usr/bin/env python3

import socket
import selectors
import types

selector = selectors.DefaultSelector()
messages = ['This is the first message', 'This is the second message']

BUFFER_SIZE = 1024

def start_connections(host, port, num_conns):
    server_address = (host, port)
    for i in range(0, num_conns):
        connid = i + 1
        print('Starting connection {} towards {}'.format(connid, server_address))
        socket_tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # We connect using connect_ex () instead of connect ()
        socket_tcp.connect_ex(server_address)
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        data = types.SimpleNamespace(connid=connid,
                                     msg_total=sum(len(m) for m in messages),
                                     recv_total=0,
                                     messages=list(messages),
                                     outb=b'')
        selector.register(socket_tcp, events, data=data)
    events = selector.select()
    for key, mask in events:
        service_connection(key, mask)
    
def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(BUFFER_SIZE)
        if recv_data:
            print('Received {} from connection {}'.format(repr(recv_data), data.connid))
            data.recv_total += len(recv_data)
        if not recv_data or data.recv_total == data.msg_total:
            print('Closing connection', data.connid)
            selector.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0).encode()
        if data.outb:
            print('Sending {} to connection {}'.format(repr(data.outb), data.connid))
            sent = sock.send(data.outb)
            data.outb = data.outb[sent:]
if __name__ == '__main__':
        host = 'localhost'
        port = 12345
        BUFFER_SIZE = 1024
        start_connections(host, port, 2)