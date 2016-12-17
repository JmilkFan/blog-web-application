import re

from flask_wtf import Form, RecaptchaField
from wtforms import (
    widgets,
    StringField,
    TextField,
    TextAreaField,
    PasswordField,
    BooleanField,
    ValidationError
)
from wtforms.validators import DataRequired, Length, EqualTo, URL

from jmilkfansblog.models import User


class CommentForm(Form):
    """Comment Form"""

    # Set some field(InputBox) for enter the data.
    # patam validators: setup list of validators
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)])

    text = TextField(u'Comment', validators=[DataRequired()])


class LoginForm(Form):
    """Login Form"""

    username = StringField('Usermame', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")

    def validate(self):
        """Validator for check the account information."""
        check_validata = super(LoginForm, self).validate()

        # If validator no pass
        if not check_validata:
            return False

        # Check the user whether exist.
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password.')
            return False

        # Check the password whether right.
        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid username or password.')
            return False

        return True


class RegisterForm(Form):
    """Register Form."""

    username = StringField('Username', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    comfirm = PasswordField('Confirm Password', [DataRequired(), EqualTo('password')])
    recaptcha = RecaptchaField()

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        # If validator no pass
        if not check_validate:
            return False

        # Check the user whether exist.
        user = User.query.filter_by(username=self.username.data).first()
        if user:
            self.username.errors.append('User with that name already exists.')
            return False
        return True


class PostForm(Form):
    """Post Form."""

    title = StringField('Title', [DataRequired(), Length(max=255)])
    text = TextAreaField('Blog Content', [DataRequired()])


class CKTextAreaWidget(widgets.TextArea):
    """CKeditor form for Flask-Admin."""

    def __call__(self, field, **kwargs):
        """Define callable type(class)."""

        # Add a new class property ckeditor: `<input class=ckedior ...>`
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(TextAreaField):
    """Create a new Field type."""

    # Add a new widget `CKTextAreaField` inherit from TextAreaField.
    widget = CKTextAreaWidget()


class OpenIDForm(Form):
    """OpenID Form."""

    openid_url = StringField('OpenID URL', [DataRequired(), URL()])


def custom_email(form_object, field_object):
    """Define a vaildator"""
    if not re.match(r"[^@+@[^@]+\.[^@]]+", field_object.data):
        raise ValidationError('Field must be a valid email address.')
