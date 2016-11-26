from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand

from jmilkfansblog import app
from jmilkfansblog import models


# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
migrate =Migrate(app, models.db)

# Create some new commands
manager.add_command("server", Server(host='127.0.0.1', port=8089))
manager.add_command("db", MigrateCommand)


@manager.shell
def make_shell_context():
    """Create a python CLI.

    return: Default import object
    type: `Dict`
    """
    return dict(app=app,
                db=models.db,
                User=models.User,
                Post=models.Post,
                Comment=models.Comment,
                Tag=models.Tag,
                Server=Server)

if __name__ == '__main__':
    manager.run()
