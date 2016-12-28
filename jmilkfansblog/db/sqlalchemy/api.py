from os import path

from oslo_config import cfg

from sqlalchemy import create_engine
import sqlalchemy.orm
from sqlalchemy.orm import exc as sqlal_exc

from jmilkfansblog.db.sqlalchemy import models


sqlalchemy_group = cfg.OptGroup(name='flask_sqlalchemy')
sqlalchemy_uri_opt = cfg.StrOpt('SQLALCHEMY_DATABASE_URI',
                                help='SQLAlchemy URI.')

CONF = cfg.CONF
CONF.register_group(sqlalchemy_group)
CONF.register_opt(sqlalchemy_uri_opt, sqlalchemy_group)

CONFIG_FILE = path.join('etc', 'jmilkfansblog.conf')
CONF(args=[], default_config_files=[CONFIG_FILE])

_ENGINE = None
_SESSION_MAKER = None


def get_engine():
    global _ENGINE
    if _ENGINE is not None:
        return _ENGINE

    _ENGINE = create_engine(CONF.flask_sqlalchemy.SQLALCHEMY_DATABASE_URI)
    # models.Base.metadata.create_all(_ENGINE)
    return _ENGINE

def get_session_maker(engine):
    global _SESSION_MAKER
    if _SESSION_MAKER is not None:
        return _SESSION_MAKER

    _SESSION_MAKER = sqlalchemy.orm.sessionmaker(bind=engine)
    return _SESSION_MAKER

def get_session():
    engine = get_engine()
    maker = get_session_maker(engine)
    session = maker()

    return session


class Connection(object):

    def __init__(self):
        self.session = get_session()

    def get_user(self, user_id):
        """Get a user via id."""
        query = self.session.query(models.User).filter_by(id=user_id)
        try:
            user = query.one()
        except sqlal_exc.NoResultFound:
            raise 
        return user

    def list_users(self):
        """Get a list the users."""
        query = self.session.query(models.User)
        users = query.all()
        return users

    def post_get_all(self):
        """Get a list of posts."""
        posts = self.session.query(models.Post).all()
        return posts
