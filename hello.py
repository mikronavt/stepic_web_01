__author__ = 'User'
import wsgiref.handlers


def app(environ, start_response):
# бизнес-логика
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
