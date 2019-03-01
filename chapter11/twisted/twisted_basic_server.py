#!/usr/bin/python3

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class MessageLogger(Protocol):

	def connectionMade(self):
		print('Client connection from:', self.transport.client)
	
	def connectionLost(self, reason):
		print('Client disconnected from:', self.transport.client)
		
	def dataReceived(self, data):
		self.transport.write(data)
		print("Message sent by the client: ", data.decode("utf-8"))

class MessageFactory(Factory):

	def buildProtocol(self, addr):
		return MessageLogger()
		
	def clientConnectionFailed(self, connector, reason):
		print ("Connection failed")
		reactor.stop()
		
	def clientConnectionLost(self, connector, reason):
		print ("Connection lost")
		reactor.stop()

# this connects the protocol to a server running on port 8080	
if __name__ == '__main__':
	#factory = Factory()
	#factory.protocol = MessageLogger
	reactor.listenTCP(8080, MessageFactory())
	reactor.run()