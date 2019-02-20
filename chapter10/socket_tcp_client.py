import socket

HOST = 'www.yahoo.com'
PORT = 80
BUFSIZ = 4096
ADDR = (HOST, PORT)

if __name__ == '__main__':
	client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_sock.connect(ADDR)
	while True:
		data = 'GET / HTTP/1.0\r\n\r\n'
		if not data:
			break
		client_sock.send(data.encode('utf-8'))
		data = client_sock.recv(BUFSIZ)
		if not data:
			break
		print(data.decode('utf-8'))

	client_sock.close()