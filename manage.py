import os

from flask.ext.script import Manager, Server
from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script.commands import ShowUrls, Clean

from jmilkfansblog import create_app
from jmilkfansblog import models


# Get the ENV from os_environ
env = os.environ.get('BLOG_ENV', 'dev')
# Create thr app instance via Factory Method
app = create_app('jmilkfansblog.config.%sConfig' % env.capitalize())

# Init manager object via app object
manager = Manager(app)

# Init migrate object via app and db object
migrate = Migrate(app, models.db)

# Create some new commands:
# Start the flask web server
manager.add_command("server", Server(host='localhost', port=8089))
# Manage database migrate
manager.add_command("db", MigrateCommand)
# Show all mapper of route url
manager.add_command("show-urls", ShowUrls())
# Clean alll the file of .pyc and .pyo
manager.add_command("clean", Clean())


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
                Role=models.Role,
                BrowseVolume=models.BrowseVolume,
                Reminder=models.Reminder,
                Server=Server)

if __name__ == '__main__':
    manager.run()
