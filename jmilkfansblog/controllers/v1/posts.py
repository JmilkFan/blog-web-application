from uuid import uuid4

from pecan import request, Response
from pecan import rest
from wsme import types as wtypes

from jmilkfansblog.api.expose import expose as wsexpose
from jmilkfansblog.controllers.v1.views import posts as posts_views
from jmilkfansblog.db import api as db_api


class Post(wtypes.Base):
    """Response data validation for post object"""

    id = str
    title = str
    text = wtypes.text
    user_id = str

    @classmethod
    def sample(cls, post):
        sample = cls(
            id=post.id,
            title=post.title,
            text=post.text,
            user_id=post.user_id)
        return sample


class Posts(wtypes.Base):
    """Response data validation for posts object"""

    posts = [Post]


class PostsController(rest.RestController):
    """REST controller for Posts."""

    _custom_actions = {
        'detail': ['GET']}

    def __init__(self):
        super(PostsController, self).__init__()
        self.posts_views = posts_views.ViewBuilder()

    @wsexpose(Posts)
    def get(self):
        """Get a list of the posts."""

        # FIXME(JmilkFan): Support Chinese
        posts = db_api.post_get_all()
        return Posts(posts=[Post.sample(post) for post in posts])

    @wsexpose()
    def get_one(self):
        pass

    @wsexpose()
    def post(self):
        pass

    @wsexpose()
    def patch(self):
        pass

    @wsexpose()
    def delete(self):
        pass

    @wsexpose()
    def detail(self):
        return "Detailed information."
