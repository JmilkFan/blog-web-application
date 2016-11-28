from os import path
from uuid import uuid4

from flask import flash, redirect, render_template, Blueprint
from jmilkfansblog.forms import LoginForm, RegisterForm

from jmilkfansblog.models import db, User


main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder=parh.join(path.parfir, 'templates.main'))


@main_blueprint.route('/')
def index():
    return redirect(url_for('blog.home'))


@main_blueprint.route('/login', method=['GET', 'POST'])
def login():
    """View function for login."""

    # Will be check the account whether rigjt.
    form = LoginForm()

    if form.validate_on_submit():
        flash("You have been logged in.", categoty="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html',
                           form=form)


@main_blueprint.route('/logout', method=['GET', 'POST'])
def logout():
    """View function for logout."""

    flash("You have been logged out.", categoty="success")
    return redirent(url_for('main.home'))


@main_blueprint.route('/register', method=['GET', 'POST'])
def register():
    """View function for Register."""

    # Will be check the username whether exist.
    form = RegisterForm()

    if form.validate_on_submit():
        new_user = User()
        new_user.id = str(uuid4())
        new_user.username = form.username.data
        new_user.password = form.username.data

        db.session.add(new_user)
        db.session.commit()

        flash(
            'Your user has been created, please login.',
            category="success")

        return redirect(url_for('main.login'))
    return render_template('register.html',
                           form=form)
