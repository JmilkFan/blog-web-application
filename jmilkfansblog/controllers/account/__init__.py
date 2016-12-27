from os import path
from uuid import uuid4

from flask import flash, url_for, redirect, render_template, Blueprint, request, session
from flask.ext.login import login_user, logout_user
from flask.ext.principal import Identity, AnonymousIdentity, identity_changed, current_app

from jmilkfansblog.forms import LoginForm, RegisterForm, OpenIDForm
from jmilkfansblog.models import db, User
from jmilkfansblog.extensions import openid, facebook, twitter


# Create the blueprint object
main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder=path.join(path.pardir, path.pardir, 'templates', 'main'))


@main_blueprint.route('/')
def index():
    """Will be default callable when request url is `/`."""
    return redirect(url_for('blog.home'))


@main_blueprint.route('/login', methods=['GET', 'POST'])
@openid.loginhandler
def login():
    """View function for login.
       
       Flask-OpenID will be receive the Authentication-information
       from relay party.
    """

    # Create the object for LoginForm
    form = LoginForm()
    # Create the object for OpenIDForm
    openid_form = OpenIDForm()

    # Send the request for login to relay party(URL).
    if openid_form.validate_on_submit():
        return openid.trg_login(
            openid_form.openid_url.data,
            ask_for=['nickname', 'email'],
            ask_for_optional=['fullname'])

    # Try to login the relay party failed.
    openid_errors = openid.fetch_error()
    if openid_errors:
        flash(openid_errors, category="danger")

    # Will be check the account whether rigjt.
    if form.validate_on_submit():

        # Using session to check the user's login status
        # Add the user's name to cookie.
        # session['username'] = form.username.data

        user = User.query.filter_by(username=form.username.data).one()

        # Using the Flask-Login to processing and check the login status for user
        # Remember the user's login status. 
        login_user(user, remember=form.remember.data)

        identity_changed.send(
            current_app._get_current_object(),
            identity=Identity(user.id))

        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html',
                           form=form,
                           openid_form=openid_form)


@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""

    # Remove the username from the cookie.
    # session.pop('username', None)

    # Using the Flask-Login to processing and check the logout status for user.
    logout_user()

    identity_changed.send(
        current_app._get_current_object(),
        identity=AnonymousIdentity())
    flash("You have been logged out.", category="success")
    return redirect(url_for('main.login'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
@openid.loginhandler
def register():
    """View function for Register."""

    # Create the form object for RegisterForm.
    form = RegisterForm()
    # Create the form object for OpenIDForm.
    openid_form = OpenIDForm()

    # Send the request for login to relay party(URL).
    if openid_form.validate_on_submit():
        return openid.try_login(
            openid_from.openid_url.data,
            ask_for=['nickname', 'email'],
            ask_for_optional=['fullname'])

    # Try to login the relay party failed.
    openid_errors = openid.fetch_error()
    if openid_errors:
        flash(openid_errors, category='danger')

    # Will be check the username whether exist.
    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Your user has been created, please login.',
              category="success")

        return redirect(url_for('main.login'))
    return render_template('register.html',
                           form=form,
                           openid_form=openid_form)


@main_blueprint.route('/facebook')
def facebook_login():
    return facebook.authorize(
        callback=url_for('main.facebook_authorized',
                         next=request.referrer or None,
                         _external=True))


@main_blueprint.route('/facebook/authorized')
@facebook.authorized_handler
def facebook_authorized(resp):
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description'])

    session['facebook_oauth_token'] = (resp['access_token'], '')

    me = facebook.get('/me')

    if me.data.get('first_name', False):
        facebook_username = me.data['first_name'] + " " + me.data['last_name']
    else:
        facebook_username = me.data['name']

    user = User.query.filter_by(username=facebook_username).first()
    if user is None:
        user = User(username=facebook_username, password='jmilkfan')
        db.session.add(user)
        db.session.commit()

    flash('You have been logged in.', category='success')

    return redirect(url_for('blog.home'))
    # FIXME(Jmilk Fan): Use the request.args.get('next') == 'http://localhost:8089/blog/'
    #return redirect(
    #    request.args.get('next') or url_for('blog.home'))


@main_blueprint.route('/twitter-login')
def twitter_login():
    return twitter.authorize(
        callback=url_for(
            'main.twitter_authorized',
            next=request.referrer or None,
            _external=True))


@main_blueprint.route('/twitter-login/authorized')
@twitter.authorized_handler
def twitter_authorized(resp):
    if resp is None:
        return 'Access denied: reason: {} error:{}'.format(
            request.args['error_reason'],
            request.args['error_description'])

    session['twitter_oauth_token'] = resp['oauth_token'] + \
        resp['oauth_token_secret']

    user = User.query.filter_by(
        username=resp['screen_name']).first()

    if not user:
        user = User(username = resp['screen_name'], password='jmilkfan')
        db.session.add(user)
        db.session.commit()


    flash("You have been logged in.", category="success")
    return redirect(
        request.args.get('next') or url_for('blog.home'))
