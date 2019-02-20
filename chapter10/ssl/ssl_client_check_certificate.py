#!/usr/bin/env python3

import socket, ssl, sys
from pprint import pprint

TARGET_HOST = 'www.google.com'
SSL_PORT = 443

# Use the path of CA certificate file in your system
CA_CERT_PATH = 'certfiles.crt'
	
if __name__ == '__main__':
	hostname = input("Enter target host:") or TARGET_HOST
	client_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client_sock.connect((hostname, 443))
	# Turn the socket over to the SSL library
	ssl_socket = ssl.wrap_socket(client_sock, ssl_version=ssl.PROTOCOL_TLSv1,cert_reqs=ssl.CERT_REQUIRED, ca_certs=CA_CERT_PATH)
	print(ssl_socket.cipher())
	try:
		ssl.match_hostname(ssl_socket.getpeercert(), hostname)
	except ssl.CertificateError as ce:
		print('Certificate error:', str(ce))
		sys.exit(1)
	print("Extracting remote host certificate details:")
	cert = ssl_socket.getpeercert()
	pprint(cert)
	ssl_socket.close()
	client_sock.close()

