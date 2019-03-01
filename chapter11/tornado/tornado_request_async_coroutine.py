#!/usr/bin/python3

import tornado.ioloop
import tornado.web
import tornado.httpclient

class Handler(tornado.web.RequestHandler):
	@tornado.web.asynchronous
	@tornado.gen.coroutine
	def get(self):
		http_client = tornado.httpclient.AsyncHTTPClient()
		response = yield tornado.gen.Task(http_client.fetch, "https://www.google.com/search?q=python")
		self.write(response.body)

if __name__ == '__main__':
	app = tornado.web.Application([tornado.web.url(r"/", Handler)])
	app.listen(8080)
	tornado.ioloop.IOLoop.current().start()