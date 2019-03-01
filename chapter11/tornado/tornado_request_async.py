#!/usr/bin/python3

import tornado.ioloop
import tornado.web
import tornado.httpclient

class Handler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
       http_client = tornado.httpclient.AsyncHTTPClient()
       http_client.fetch("https://www.google.com/search?q=python", callback=self.on_response)

    def on_response(self, response):
       self.write(response.body)
       self.finish()

if __name__ == '__main__':	   
	app = tornado.web.Application([ tornado.web.url(r"/", Handler)])
	app.listen(8080)
	tornado.ioloop.IOLoop.current().start()