import pecan

from jmilkfansblog.api import config as api_config
from jmilkfansblog.api import hooks


def get_pecan_config():
    """Load the Pecan config from config.py."""

    filename = api_config.__file__.replace('.pyc', '.py')
    return pecan.configuration.conf_from_file(filename)


def setup_app(config=None):
    """Create a WSGI application object."""

    if not config:
        config = get_pecan_config()

    # Setup the hooks for WSGI Application(Like Middleware in Paste).
    #    EG. app_hooks = [hooks.DBHook()]
    app_hooks = []
    # Setup the config for WSGI Application.
    app_conf = dict(config.app)

    # Create and init the WSGI Application.
    app = pecan.make_app(
        app_conf.pop('root'),
        logging=getattr(config, 'logging', {}),
        hooks=app_hooks,
        **app_conf
    )
    return app


def app_factory(global_config, **local_conf):
    return setup_app()
