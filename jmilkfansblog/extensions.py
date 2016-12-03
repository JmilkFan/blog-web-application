from uuid import uuid4

from flask.ext.bcrypt import Bcrypt
from flask.ext.openid import OpenID
from flask_oauth import OAuth


# Create the Flask-Bcrypt's instance
bcrypt = Bcrypt()
# Create the Flask-OpenID's instance
openid = OpenID()
# Create the Flask-OAuth's instance
oauth = OAuth()

# Create the auth object for facebook.
facebook = oauth.remote_app(
    'facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key='<FACEBOOK_APP_ID>',
    consumer_secret='<FACEBOOK_APP_SECRET>',
    request_token_params={'scope': 'email'})

twitter = oauth.remote_app(
    'twitter',
    base_url='https://api.twitter.com/1.1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key='<TWITTER_APP_ID>',
    consumer_secret='<TWITTER_APP_SECRET>')


@openid.after_login
def create_or_login(resp):
    """Will be execute after login."""

    from jmilkfansblog.models import db, User

    usernmae = resp.fullname or resp.nickname or resp.email
    if not username:
        flash('Invalid login. Please try again.', 'danger')
        return redirect(url_for('main.login'))

    user = User.query.filter_by(username=usernmae).first()
    if user is None:
        user = User(id=str(uuid4()), username=username, password='jmilkfan')
        db.session.add(user)
        db.session.commit()

    return redirect(url_for('blog.home'))


@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_oauth_token')
