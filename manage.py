# import Flask Script object
from flask.ext.script import Manager, Server
import main

# Init manager object via app object
manager = Manager(main.app)

# Create some new commands
manager.add_command("server", Server())

@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=main.app)

if __name__ == '__main__':
    manager.run()
