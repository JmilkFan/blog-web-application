from uuid import uuid4

from pecan import request, Response
from pecan import rest
from wsme import types as wtypes

from jmilkfansblog.api.expose import expose as wsexpose
from jmilkfansblog.controllers.v1.views import posts as posts_views


class Post(wtypes.Base):
    """Response data validation for post object"""

    id = str
    title = str
    text = wtypes.text
    user_id = str


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

        db_conn = request.db_conn
        posts = db_conn.post_get_all()
        posts_list = []
        for post in posts:
            post_val = Post()
            post_val.id = post.id
            post_val.title = post.title
            post_val.text = post.text
            post_val.user_id = post.user_id
            posts_list.append(post_val)
        # FIXME(JmilkFan): Support Chinese
        return Posts(posts=posts_list)
            

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
