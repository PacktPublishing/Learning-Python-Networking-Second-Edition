#!/usr/bin/env python3

from twisted.internet import reactor
from twisted.web import server, resource

class TwistedResource(resource.Resource):
        def render_GET(self, request):
                return b"<html><center><h1>Twisted server is running on port 8080</h1></center></html>"

root = resource.Resource()
root.putChild(b"twisted", TwistedResource())
site = server.Site(root)
reactor.listenTCP(8080, site)
reactor.run()

