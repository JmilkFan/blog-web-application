from wsgiref import simple_server

from jmilkfansblog.api import wsgi_app

def main():
    host = '127.0.0.1'
    port = 8080

    # Create the WSGI application object.
    wsgi_application = wsgi_app.setup_app()
    # Create the Simple process server.
    server = simple_server.make_server(host, port, wsgi_application)

    server.serve_forever()


if __name__ == '__main__':
    main()
