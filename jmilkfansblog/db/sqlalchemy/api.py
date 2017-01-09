"""Implementation of SQLAlchemy backend."""
import sys

from oslo_config import cfg
from oslo_db.sqlalchemy import session as db_session

from jmilkfansblog.db.sqlalchemy import models


CONF = cfg.CONF

_FACADE = None


def _create_facade_lazily():
    global _FACADE
    if _FACADE is None:
        _FACADE = db_session.EngineFacade(
            # FIXME(Fan Guiju): Can't be use: CONF.database.connection
            # db.api ==> db.sqlalchemy.api
            CONF.database.connection,
            **dict(CONF.database))
    return _FACADE


def get_engine():
    return _create_facade_lazily().get_engine()


def get_session(**kwargs):
    return _create_facade_lazily().get_session(**kwargs)


def get_backend():
    """Define the SQLAlchemy Backend Implements."""

    return sys.modules[__name__]
    #    This module is the Backend Implements.
    #    Don't need to Create the class `SQLAlchemyClass`
    #    and define the functions in it.
    # return Connection


def dispose_engine():
    get_engine().dispose()


def user_get_all():
    session = get_session()
    with session.begin():
        users = session.query(models.User).all()
    return users


def post_get_all():
    session = get_session()
    with session.begin():
        posts = session.query(models.Post).all()
    return posts
