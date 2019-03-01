#!/usr/bin/python3

import argparse
import tornado.ioloop
import tornado.httpclient

class TornadoAsyncClient():
    def handle_request(self,response):
        if response.error:
            print ("Error:", response.error)
        else:
            print (response.body)
        tornado.ioloop.IOLoop.instance().stop()

def run_server(url):
    tornadoAsync = TornadoAsyncClient()
    http_client = tornado.httpclient.AsyncHTTPClient()
    http_client.fetch(url, tornadoAsync.handle_request)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Tornado async client')
    parser.add_argument('--url', action="store", dest="url", type=str, required=True)
    given_args = parser.parse_args() 
    url = given_args.url
    run_server(url)
