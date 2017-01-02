import datetime
from uuid import uuid4

from flask.ext.restful import Resource, fields, marshal_with 
from flask import abort
from jmilkfansblog.models import db, User, Post, Tag
from jmilkfansblog.controllers.flask_restful import fields as jf_fields
from jmilkfansblog.controllers.flask_restful import parsers


# String format output of tag
nested_tag_fields = {
    'id': fields.String(),
    'name': fields.String()}

# String format output of post
post_fields = {
    # x == object of post
    'id': fields.String(),
    'author': fields.String(attribute=lambda x: x.user.username),
    'title': fields.String(),
    'text': jf_fields.HTMLField(),
    'tags': fields.List(fields.Nested(nested_tag_fields)),
    'publish_date': fields.DateTime(dt_format='iso8601')}


class PostApi(Resource):
    """Restful API of posts resource."""

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
            args = parsers.post_get_parser.parse_args()
            page = args['page'] or 1

            # Return the posts with user.
            if args['user']:
                user = User.query.filter_by(username=args['user']).first()
                if not user:
                    abort(404)
                posts = user.posts.order_by(
                    Post.publish_date.desc()).paginate(page, 30)
            # Return the posts.
            else:
                posts = Post.query.order_by(
                    Post.publish_date.desc()).paginate(page, 30)

            return posts.items

    def post(self, post_id=None):
        """Can be execute when receive HTTP Method `POST`.
        """

        if post_id:
            abort(400)
        else:
            args = parsers.post_post_parser.parse_args(strict=True)

            # Validate the user identity via token(/api/auth POST).
            # Will be create the post(/api/posts POST), if pass with validate token.
            user = User.verify_auth_token(args['token'])
            if not user:
                abort(401)

            new_post = Post()
            new_post.title = args['title']
            new_post.date = datetime.datetime.now()
            new_post.text = args['text']
            new_post.user = user

            if args['tags']:
                for item in args['tags']:
                    tag = Tag.query.filter_by(name=item).first()
                    # If the tag already exist, append.
                    if tag:
                        new_post.tags.append(tag)
                    # If the tag not exist, create the new one.
                    # Will be write into DB with session do.
                    else:
                        new_tag = Tag()
                        new_tag.name = item
                        new_post.tags.append(new_tag)

        db.session.add(new_post)
        db.session.commit()
        return (new_post.id, 201)

    def put(self, post_id=None):
        """Will be execute when receive the HTTP Request Methos `PUT`.""" 
 
        if not post_id:
            abort(400)
 
        post = Post.query.filter_by(id=post_id).first()
        if not post:
            abort(404)
 
        args = parsers.post_put_parser.parse_args()
        user = User.verify_auth_token(args['token'])

        if not user:
            abort(401)
        if user != post.user:
            abort(403)

        if args['title']:
            post.title = args['title']
        if args['text']:
            post.text = args['text']
        if args['tags']:
            for item in args['tags']:
                tag = Tag.query.filter_by(name=item).first()
                if tag:
                    post.tags.append(tag)
                else:
                   new_tag = Tag()
                   new_tag.name = item
                   post.tags.append(new_tag)

        db.session.add(post)
        db.session.commit()

        return (post.id, 201)

    def delete(self, post_id=None):
        """Will be execute when receive the HTTP Request Method `DELETE`."""

        if not post_id:
            abort(400)

        post = Post.query.filter_by(id=post_id).first()
        if not post:
            abort(404)

        args = parsers.post_delete_parser.parse_args(strict=True)
        user = User.verify_auth_token(args['token'])
        if user != post.user:
            abort(403)

        # Will be delete relationship record with posts_tags too.
        # But you have to ensure the number of record equal with len(post.tags)
        db.session.delete(post)
        db.session.commit()

        return "", 204
