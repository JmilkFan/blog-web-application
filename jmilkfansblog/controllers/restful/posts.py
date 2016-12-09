from flask.ext.restful import Resource, fields, marshal_with 
from flask import abort
from jmilkfansblog.models import Post
from jmilkfansblog.controllers.restful import fields as jf_fields


# String format output of tag
nested_tag_fields = {
    'id': fields.String(),
    'name': fields.String()}

# String format output of post
post_fields = {
    'author': fields.String(attribute=lambda x: x.users.username),
    'title': fields.String(),
    'text': jf_fields.HTMLField(),
    'tags': fields.List(fields.Nested(nested_tag_fields)),
    'publish_date': fields.DateTime(dt_format='iso8601')}


class PostApi(Resource):
    """Restful API of Post."""

    @marshal_with(post_fields)
    def get(self, post_id=None):
        """Can be execute when receive HTTP Method `GET`.
           Will be return the Dict object as post_fields.
        """

        if post_id:
            post = Post.query.filter_by(id=post_id).first()
            if not post:
                abort(404)
            return post
        else:
            posts = Post.query.all()
            return posts
