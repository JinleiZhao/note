def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    print(environ)
    print(start_response)
    return [b'<h1>Hello, web!</h1>']
