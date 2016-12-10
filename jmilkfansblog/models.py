from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import BadSignature, SignatureExpired
from uuid import uuid4

from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import AnonymousUserMixin
from flask.ext.principal import current_app

from jmilkfansblog.extensions import bcrypt


# Create the db object
# Init the db from jmilkfansblog/__init__py
db = SQLAlchemy()

posts_tags = db.Table('posts_tags',
    db.Column('post_id', db.String(45), db.ForeignKey('posts.id')),
    db.Column('tag_id', db.String(45), db.ForeignKey('tags.id')))

users_roles = db.Table('users_roles',
    db.Column('user_id', db.String(45), db.ForeignKey('users.id')),
    db.Column('role_id', db.String(45), db.ForeignKey('roles.id')))


class User(db.Model):
    """Represents Proected users."""

    # Set the name for table
    __tablename__ = 'users'
    id = db.Column(db.String(45), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))
    # one to many: User ==> Post 
    # Establish contact with Post's ForeignKey: user_id
    # (FIXME): Relationship of User and Post is one to many,
    #          So backref="user".
    posts = db.relationship(
        'Post',
        backref='users',
        lazy='dynamic')

    roles = db.relationship(
        'Role',
        secondary=users_roles,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = self.set_password(password)

        # Setup the default-role for user.
        default = Role.query.filter_by(name="default").one()
        self.roles.append(default)

    def __repr__(self):
        """Define the string format for instance of User."""
        return "<Model User `{}`>".format(self.username)

    def set_password(self, password):
        """Convert the password to cryptograph via flask-bcrypt"""
        return bcrypt.generate_password_hash(password)

    def check_password(self, password):
        """Check the entry-password whether as same as user.password."""
        return bcrypt.check_password_hash(self.password, password)

    def is_authenticated(self):
        """Check the user whether logged in."""

        # Check the User's instance whether Class AnonymousUserMixin's instance.
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active():
        """Check the user whether pass the activation process."""

        return True

    def is_anonymous(self):
        """Check the user's login status whether is anonymous."""

        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        """Get the user's uuid from database."""

        return unicode(self.id)

    @staticmethod
    def verify_auth_token(token):
        """Validate the token whether is night."""

        serializer = Serializer(
            current_app.config['SECRET_KEY'])
        try:
            # serializer object already has tokens in itself and wait for 
            # compare with token from HTTP Request /api/posts Method `POST`.
            data = serializer.loads(token)
        except SignatureExpired:
            return None
        except BadSignature:
            return None

        user = User.query.filter_by(id=data['id']).first()
        return user


class Role(db.Model):
    """Represents Proected roles."""

    __tablename__ = 'roles'

    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Role `{}`>".format(self.name)


class Post(db.Model):
    """Represents Proected posts."""

    __tablename__ = 'posts'
    id = db.Column(db.String(45), primary_key=True)
    title = db.Column(db.String(255))
    text = db.Column(db.Text())
    publish_date = db.Column(db.DateTime)
    # Set the foreign key for Post
    user_id = db.Column(db.String(45), db.ForeignKey('users.id'))
    # one to many: Post ==> Comment
    # Establish contact with Comment's ForeignKey: post_id
    comments = db.relationship(
        'Comment',
        backref='posts',
        lazy='dynamic')
    # many to many: posts <==> tags
    # Association table: posts_tags
    tags = db.relationship(
        'Tag',
        secondary=posts_tags,
        backref=db.backref('posts', lazy='dynamic'))
    
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def __repr__(self):
        return "<Model Post `{}`>".format(self.title)


class Comment(db.Model):
    """Represents Proected comments."""

    __tablename__ = 'comments'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))
    text = db.Column(db.Text())
    date = db.Column(db.DateTime())
    post_id = db.Column(db.String(45), db.ForeignKey('posts.id'))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return '<Model Comment `{}`>'.format(self.name)


class Tag(db.Model):
    """Represents Proected tags."""

    __tablename__ = 'tags'
    id = db.Column(db.String(45), primary_key=True)
    name = db.Column(db.String(255))

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return "<Model Tag `{}`>".format(self.name)


class BrowseVolume(db.Model):
    """Represents Proected browse_volumes."""

    __tablename__ = 'browse_volumes'
    id = db.Column(db.String(45), primary_key=True)
    home_view_total = db.Column(db.Integer)

    def __init__(self, id):
        self.id = id
        self.home_view_total = 0

    def __repr__(self):
        return '<Model BrowseVolume `{}`>'.format(self.home_view_total)

    def add_one(self):
        self.home_view_total += 1
