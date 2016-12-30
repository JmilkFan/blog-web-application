"""Implementation of SQLAlchemy backend."""

from oslo_config import cfg
from oslo_db.sqlalchemy import session as db_session

from jmilkfansblog.db.sqlalchemy import models

CONF = cfg.CONF
# Import the config option group `database` from jmilkfansblog.config
CONF.import_group('database', 'jmilkfansblog.config')

_FACADE = None


def _create_facade_lazily():
    global _FACADE
    if _FACADE is None:
        _FACADE = db_session.EngineFacade(
            CONF.database.connection,
            **dict(CONF.database))
    return _FACADE


def get_engine():
    return _create_facade_lazily().get_engine()


def get_session(**kwargs):
    return _create_facade_lazily().get_session(**kwargs)


def get_backend():
    """Define the SQLAlchemy Backend Implements."""

    # return sys.modules[__name__]
    #    This module is the Backend Implements.
    #    Don't need to Create the class `SQLAlchemyClass`
    #    and define the functions in it.
    return Connection


def dispose_engine():
    get_engine().dispose()


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
