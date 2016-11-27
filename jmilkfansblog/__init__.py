from flask import Flask, redirect, url_for

from jmilkfansblog.models import db
from jmilkfansblog.controllers import blog
from jmilkfansblog.extensions import bcrypt


def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    app = Flask(__name__)
    # Set the config for app instance
    app.config.from_object(object_name)
    
    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)
    # Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)
    
    
    @app.route('/')
    def index():
        # Redirect the Request_url '/' to '/blog/'
        return redirect(url_for('blog.home'))
    
    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)

    return app
