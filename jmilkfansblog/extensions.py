from uuid import uuid4

from flask import session
from flask.ext.bcrypt import Bcrypt
from flask.ext.openid import OpenID
from flask_oauth import OAuth
from flask.ext.login import LoginManager
from flask.ext.principal import Principal, Permission, RoleNeed
from flask.ext.restful import Api
from flask.ext.celery import Celery
from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.cache import Cache
from flask_assets import Environment, Bundle
from flask.ext.admin import Admin
from flask_mail import Mail
from flask_youku import Youku
from flask_gzip import GZip


#### Create the Flask-Bcrypt's instance
bcrypt = Bcrypt()

#### Create the Flask-OpenID's instance
openid = OpenID()

#### Create the Flask-Principal's instance
principals = Principal()

#### Create the Flask-Restful's instance
restful_api = Api()

#### Create the Flask-Celery-Helper's instance
flask_celery = Celery()

#### Create the Flask-DebugToolbar's instance
debug_toolbar = DebugToolbarExtension()

#### Create the Flask-Cache's instance
cache = Cache()

#### Create the Flask-Admin's instance
flask_admin = Admin()

### Create the Flask-Mail's instance
mail = Mail()

#### Create the Flask-Assets's instance
assets_env = Environment()
# Define the set for js and css file.
main_css = Bundle(
    'css/bootstrap.css',
    'css/bootstrap-theme.css',
    filters='cssmin',
    output='assets/css/common.css')

main_js = Bundle(
    'js/bootstrap.js',
    filters='jsmin',
    output='assets/js/common.js')

#### Create the Flask-Login's instance
login_manager = LoginManager()
# Init the permission object via RoleNeed(Need).
admin_permission = Permission(RoleNeed('admin'))
poster_permission = Permission(RoleNeed('poster'))
default_permission = Permission(RoleNeed('default'))
# Setup the configuration for login manager.
#     1. Set the login page.
#     2. Set the more stronger auth-protection.
#     3. Show the information when you are logging.
#     4. Set the Login Messages type as `information`.
login_manager.login_view = "main.login"
login_manager.session_protection = "strong"
login_manager.login_message = "Please login to access this page."
login_manager.login_message_category = "info"
# login_manager.anonymous_user = CustomAnonymousUser

#### Create the Flask-OAuth's instance
oauth = OAuth()
# Create the auth object for facebook.
facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='1634926073468088',
    consumer_secret='a45ec6096ad272c4d61788b912a66394',
    request_token_params={'scope': 'email'})
# Create the auth object for twitter.
twitter = oauth.remote_app(
    'twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='<TWITTER_APP_ID>',
    consumer_secret='<TWITTER_APP_SECRET>')

#### Create the Flask-Youku's instance
youku = Youku()

#### Create the Flask-Gzip's instance
flask_gzip = GZip()


@openid.after_login
def create_or_login(resp):
    """Will be execute after pass the auth via openid."""

    from jmilkfansblog.models import db, User

    usernmae = resp.fullname or resp.nickname or resp.email
    if not username:
        flash('Invalid login. Please try again.', 'danger')
        return redirect(url_for('main.login'))

    user = User.query.filter_by(username=usernmae).first()
    if user is None:
        user = User(username=username, password='jmilkfan')
        db.session.add(user)
        db.session.commit()

    # Logged in via OpenID.
    return redirect(url_for('blog.home'))


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_oauth_token')


@twitter.tokengetter
def get_twitter_token():
    return session.get('twitter_oauth_token')


@login_manager.user_loader
def load_user(user_id):
    """Load the user's info."""

    from models import User
    return User.query.filter_by(id=user_id).first()
