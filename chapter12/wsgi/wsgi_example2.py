#!/usr/bin/env python3

from wsgiref.simple_server import make_server

def page(content, *args):
    yield b'<html><head><title>wsgi_example.py</title></head><body>'
    yield (content % args).encode('utf-8')
    yield b'</body></html>'

def application(environ, start_response):

    if environ['PATH_INFO'] == '/':
        response = "<p>This is my web page built with python wsgi</p>"
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return page(response)

    elif environ['PATH_INFO'] == '/operation':

        print('environ["QUERY_STRING"]:',environ["QUERY_STRING"])
        params = environ["QUERY_STRING"].split("&")
        print('Parameters ',params)
        operator1 = params[0].split("=")[1]
        print('Operator 1:',operator1)
        operator2 = params[1].split("=")[1]
        print('Operator 2:',operator2)
        operation = params[2].split("=")[1]
        print('Operation:',operation)
        result = str(eval(operator1+operation+operator2))
        print('Result:',result)
        response = "<p>The operation result is %s</p>" %result
        start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')])
        return page(response)

    else:
        response = "<p>This URL is not valid</p>"
        start_response('404 Not Found', [('Content-Type', 'text/html; charset=utf-8')])
        return page(response)

if __name__ == '__main__':
    print('Listening on localhost:8080')
    server = make_server('localhost', 8080, application)
    server.serve_forever()
