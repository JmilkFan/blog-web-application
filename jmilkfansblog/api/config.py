from jmilkfansblog.api import hooks

"""Setup the Pecan application config."""

app = {
    # Define the controller path of pecan_root.py, 
    # entry_point for application, analysis the URL `/`
    'root': 'jmilkfansblog.controllers.root.RootController',

    # Define the modules directory of pecan
    'modules': ['jmilkfansblog.api'],
    'debug': False

    # Setup the class list of hooks.
    # Don't need setup again, if setup on the setup_app() in wsgi_app.py
    # 'hooks': [hooks.DBHook()],
}
