from os import path
from uuid import uuid4

from flask import flash, url_for, redirect, render_template, Blueprint
from jmilkfansblog.forms import LoginForm, RegisterForm

from jmilkfansblog.models import db, User


# Create the blueprint object
main_blueprint = Blueprint(
    'main',
    __name__,
    template_folder=path.join(path.pardir, 'templates', 'main'))


@main_blueprint.route('/')
def index():
    """Will be default callable when request url is `/`."""
    return redirect(url_for('blog.home'))


@main_blueprint.route('/login', methods=['GET', 'POST'])
def login():
    """View function for login."""

    # Create the form object
    form = LoginForm()

    # Will be check the account whether rigjt.
    if form.validate_on_submit():
        flash("You have been logged in.", category="success")
        return redirect(url_for('blog.home'))

    return render_template('login.html',
                           form=form)


@main_blueprint.route('/logout', methods=['GET', 'POST'])
def logout():
    """View function for logout."""

    flash("You have been logged out.", category="success")
    return redirect(url_for('blog.home'))


@main_blueprint.route('/register', methods=['GET', 'POST'])
def register():
    """View function for Register."""

    # Create the form object.
    form = RegisterForm()

    # Will be check the username whether exist.
    if form.validate_on_submit():
        new_user = User(id=str(uuid4()),
                        username=form.username.data,
                        password=form.password.data)

        db.session.add(new_user)
        db.session.commit()

        flash('Your user has been created, please login.',
              category="success")

        return redirect(url_for('main.login'))
    return render_template('register.html',
                           form=form)
