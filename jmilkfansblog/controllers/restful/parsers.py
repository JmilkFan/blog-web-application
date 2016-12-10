from flask.ext.restful import reqparse


########################################################
# Post's HTTP Request Parser
########################################################

post_get_parser = reqparse.RequestParser()
post_post_parser = reqparse.RequestParser()
post_put_parser = reqparse.RequestParser()
post_delete_parser = reqparse.RequestParser()

post_get_parser.add_argument(
    'page',
    type=int,
    location=['json', 'args', 'headers'],
    required=False)

post_get_parser.add_argument(
    'user',
    type=str,
    location=['json', 'args', 'headers'])

post_post_parser.add_argument(
    'title',
    type=str,
    required=True,
    help='Title is required!')

post_post_parser.add_argument(
    'text',
    type=str,
    required=True,
    help='Text is required!')

post_post_parser.add_argument(
    'tags',
    type=str,
    action='append')

post_post_parser.add_argument(
    'token',
    type=str,
    required=True,
    help='Auth Token is required to create posts.')

post_put_parser.add_argument(
    'title',
    type=str)

post_put_parser.add_argument(
    'text',
    type=str)

post_put_parser.add_argument(
    'tags',
    type=str,
    action='append')

post_put_parser.add_argument(
    'token',
    type=str,
    required=True,
    help='Auth Token is required to update the posts.')

post_delete_parser.add_argument(
    'token',
    type=str,
    required=True,
    help='Auth Token is required to update the posts.')

########################################################
# User's HTTP Request Parser
########################################################

user_post_parser = reqparse.RequestParser()

user_post_parser.add_argument(
    'username',
    type=str,
    required=True,
    help='Username is required!')

user_post_parser.add_argument(
    'password',
    type=str,
    required=True,
    help='Password is required!')
