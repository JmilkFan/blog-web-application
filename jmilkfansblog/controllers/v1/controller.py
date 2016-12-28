from pecan import rest
from wsme import types as wtypes

from jmilkfansblog.api import expose
from jmilkfansblog.controllers.v1 import users
from jmilkfansblog.controllers.v1 import posts


class V1Controller(rest.RestController):
    """Version 1 API controller root."""

    users = users.UsersController()
    posts = posts.PostsController()

    @expose.expose(wtypes.text)
    def get(self):
        return 'jmilkfansblog v1 controller'
