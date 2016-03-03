__author__ = 'User'
import wsgiref.handlers

bind = '0.0.0.0:8080'

pythonpath= "/home/box/web"


def app(environ, start_response):
    status = '200 OK'
    headers = [
    ('Content-Type', 'text/plain')
    ]

    body = ''
    if environ['REQUEST_METHOD'] == 'GET' and environ['QUERY_STRING']:
        query = environ['QUERY_STRING'].split('&');
        for param in query:
            body += param + '\n'


    start_response(status, headers)
    return [ body ]
