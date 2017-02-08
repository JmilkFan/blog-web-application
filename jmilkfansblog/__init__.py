import os

from oslo_log import log as logging
from oslo_config import cfg

from flask import Flask, redirect, url_for
from flask.ext.login import current_user
from flask.ext.principal import identity_loaded, UserNeed, RoleNeed
from sqlalchemy import event

from jmilkfansblog.db.sqlalchemy.models import db, User, Post, Role, Tag, BrowseVolume, Reminder
from jmilkfansblog.controllers import blog
from jmilkfansblog.controllers import account
from jmilkfansblog.controllers.flask_restful.posts import PostApi
from jmilkfansblog.controllers.flask_restful.auth import AuthApi
from jmilkfansblog.extensions import bcrypt, openid, login_manager, principals, flask_celery
from jmilkfansblog.extensions import restful_api, debug_toolbar, cache, flask_admin
from jmilkfansblog.extensions import assets_env, main_js, main_css, mail, youku, flask_gzip
from jmilkfansblog.tasks import on_reminder_save
from jmilkfansblog.controllers import admin
from jmilkfansblog.i18n import _LI, _LE


LOG = logging.getLogger(__name__)

CONF = cfg.CONF


def create_app(object_name):
    """Create the app instance via `Factory Method`"""

    LOG.info(_LI("Create the flask application object %s"), object_name)

    app = Flask(__name__)
    # Set the config for app instance
    app.config.from_object(object_name)

    #### Init the Flask-SQLAlchemy via app boject
    # Will be load the SQLALCHEMY_DATABASE_URL from config.py to db object
    db.init_app(app)
    # Using the SQLAlchemy's event
    # Will be callback on_reminder_save when insert recond into table `reminder`.
    event.listen(Reminder, 'after_insert', on_reminder_save)

    #### Init the Flask-Bcrypt via app object
    bcrypt.init_app(app)

    #### Init the Flask-OpenID via app object
    openid.init_app(app)

    #### Init the Flask-Login via app object
    login_manager.init_app(app)

    #### Init the Flask-Prinicpal via app object
    principals.init_app(app)

    #### Init the Flask-Celery-Helper via app object
    # Register the celery object into app object
    flask_celery.init_app(app)

    #### Init the Flask-Restful via app object
    # Define the route of restful_api
    restful_api.add_resource(
        PostApi,
        '/api/posts',
        '/api/posts/<string:post_id>',
        endpoint='restful_api_post')

    restful_api.add_resource(
        AuthApi,
        '/api/auth',
        endpoint='restful_api_auth')
    restful_api.init_app(app)

    #### Init the Flask-DebugToolbar via app object
    debug_toolbar.init_app(app)

    #### Init the Flask-Cache via app object
    cache.init_app(app)

    #### Init the Flask-Assets via app object
    assets_env.init_app(app)
    assets_env.register('main_js', main_js)
    assets_env.register('main_css', main_css)

    #### Init the Flask-Admin via app object
    flask_admin.init_app(app)
    # Register view function `CustomView` into Flask-Admin
    flask_admin.add_view(admin.CustomView(name='Custom'))
    # Register view function `CustomModelView` into Flask-Admin
    models = [Role, Tag, Reminder, BrowseVolume]
    for model in models:
        flask_admin.add_view(
            admin.CustomModelView(model, db.session, category='Models'))
    # Register view function `PostView` into Flask-Admin
    flask_admin.add_view(
        admin.PostView(Post, db.session, name='PostManager'))
    # Register and define path of File System for Flask-Admin
    flask_admin.add_view(
        admin.CustomFileAdmin(
            os.path.join(os.path.dirname(__file__), 'static'),
            '/static',
            name='Static Files'))

    #### Init the Flask-Mail via app object
    mail.init_app(app)

    #### Init the Flask-Youku via app object
    youku.init_app(app)

    #### Init the Flask-GZip via app object
    # FIXME(Fan Guiju): UnicodeDecodeError
    #                   Have to setup the `DEBUG = False`
    # flask_gzip.init_app(app)

    @identity_loaded.connect_via(app)
    def on_identity_loaded(sender, identity):
        """Change the role via add the Need object into Role.

           Need the access the app object.
        """

        # Set the identity user object
        identity.user = current_user

        # Add the UserNeed to the identity user object
        if hasattr(current_user, 'id'):
            identity.provides.add(UserNeed(current_user.id))

        # Add each role to the identity user object
        if hasattr(current_user, 'roles'):
            for role in current_user.roles:
                identity.provides.add(RoleNeed(role.name))

    # Register the Blueprint into app object
    app.register_blueprint(blog.blog_blueprint)
    app.register_blueprint(account.main_blueprint)

    return app
