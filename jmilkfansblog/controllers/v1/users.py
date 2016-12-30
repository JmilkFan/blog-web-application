from uuid import uuid4

import pecan
from pecan import request
from pecan import rest
from wsme import types as wtypes

from jmilkfansblog.api import expose
from jmilkfansblog.db import api as db_api


class User(wtypes.Base):
    """Response data validation for user object"""
    id = str
    username = wtypes.wsattr(wtypes.text, mandatory=True)
    password = wtypes.text


class Users(wtypes.Base):
    """Response data validation for users object"""
    users = [User]


class UsersController(rest.RestController):

    @pecan.expose()
    def _lookup(self, user_id, *remainder):
        return UserController(user_id), remainder

    @expose.expose(Users)
    def get(self):

        users = db_api.user_get_all()
        users_list = []

        for user in users:
            u = User()
            u.id = user.id
            u.username = user.username
            u.password = user.password
            users_list.append(u)
        return Users(users=users_list)

    @expose.expose(None, body=User, status_code=201)
    def post(self, user):
        print user
