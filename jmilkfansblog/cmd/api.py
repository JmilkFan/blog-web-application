from os import path
from wsgiref import simple_server

from oslo_config import cfg

from jmilkfansblog.api import wsgi_app


DEFAULT_API_OPTS = [
    cfg.StrOpt('host',
               default='localhost',
               help="Ipaddress of jmilkfansblog-api."),

    cfg.IntOpt('api_port',
               default=8080,
               help="Port of jmilkfansblog-api.")]

CONF = cfg.CONF
CONF.register_opts(DEFAULT_API_OPTS)
# Specified the path of config file with CLI option `--config-file`
CONF()


def main():
    host = CONF.host
    port = CONF.api_port

    # Create the WSGI application object.
    wsgi_application = wsgi_app.setup_app()
    # Create the Simple process server.
    server = simple_server.make_server(host, port, wsgi_application)

    server.serve_forever()
