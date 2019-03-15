#!/usr/bin/python3

import tornado.ioloop
import tornado.web
from tornado.options import define, options

class MyHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")
 
if __name__ == '__main__':
	define("port", default=8080, help="run on the given port", type=int)
	app = tornado.web.Application([('/', MyHandler)])
	app.listen(options.port)
	print("Tornado web server listening on port 8080");
	tornado.ioloop.IOLoop.instance().start()