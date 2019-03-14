#!/usr/bin/env python3

from wsgiref.simple_server import make_server

def page(content, *args):
    yield b'<html><head><title>wsgi_example.py</title></head><body>'
    yield (content % args).encode('utf-8')
    yield b'</body></html>'

def application(environ, start_response):
    # I keep the output that I will return in response
    response = "<p>This is my web page built with python wsgi</p>"
    # A response to the browser is generated
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
    return page(response)

if __name__ == '__main__':
    print('Listening on localhost:8080')
    srv = make_server('localhost', 8080, application)
    srv.serve_forever()