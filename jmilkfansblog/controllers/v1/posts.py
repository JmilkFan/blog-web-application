from uuid import uuid4

import pecan
from pecan import request
from pecan import rest
from wsme import types as wtypes

from jmilkfansblog.api import expose
from jmilkfansblog.models import Post
from jmilkfansblog.controllers.v1.views import posts as posts_views


class PostsController(rest.RestController):
    """REST controller for Posts."""

    def __init__(self):
        super(PostsController, self).__init__()
        self.posts_views = posts_views.ViewBuilder()

    _custom_actions = {
        'detail': ['GET']}

    @expose.expose()
    def get_all(self):
        posts = Post.query.all()
        return self.posts_views.index(posts)
