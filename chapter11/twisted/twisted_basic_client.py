#!/usr/bin/python3

from twisted.internet import reactor
from twisted.internet.protocol import Protocol
from twisted.internet.protocol import ClientFactory

class MyTwistedClient(Protocol):
	def connectionMade(self):
		self.transport.write('Connection established'.encode())
		
	def connectionLost(self, reason):
		print('Connection Lost %s ' %(reason))

	def dataReceived(self, data):
		print('Server data: ', data)
		self.transport.loseConnection()


class MyTwistedClientFactory(ClientFactory):
	protocol = MyTwistedClient 

	def clientConnectionFailed(self, connector, reason):
		print('Connection Failed')
		reactor.stop()
	
	def clientConnectionLost(self, connector, reason):
		print('Connection Lost')
		reactor.stop()

reactor.connectTCP('localhost', 8080, MyTwistedClientFactory())
reactor.run()
