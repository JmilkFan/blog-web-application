import re

from flask_wtf import Form
from wtforms import (
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

    usermame = StringField('Usermame', [DataRequired(), Length(max=255)])
    password = PasswordField('Password', [DataRequired()])

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
            self.username.errors.append('Invalid username or password.')
            return False

        return True


def custom_email(form_object, field_object):
    """Define a vaildator"""
    if not re.match(r"[^@+@[^@]+\.[^@]]+", field_object.data):
        raise ValidationError('Field must be a valid email address.')
