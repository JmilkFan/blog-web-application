from pecan import rest
from wsme import types as wtypes

from jmilkfansblog.api.expose import expose as wsexpose
from jmilkfansblog.controllers.v1 import users
from jmilkfansblog.controllers.v1 import posts


class V1(wtypes.Base):
    id = wtypes.text
    """The ID of the version, also acts as the release number"""

    @staticmethod
    def convert():
        v1 = V1()
        v1.id = 'v1'
        return v1


class Controller(rest.RestController):
    """Version 1 API controller root."""

    users = users.UsersController()
    posts = posts.PostsController()

    @wsexpose(V1)
    def get(self):
        return V1.convert()
