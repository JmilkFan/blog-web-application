# import Flask Script object
from flask.ext.script import Manager, Server
import main
import models

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
    return dict(app=main.app,
                db=models.db,
                User=models.User,
                Post=models.Post)

if __name__ == '__main__':
    manager.run()
