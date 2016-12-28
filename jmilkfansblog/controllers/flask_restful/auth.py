from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

from flask import abort, current_app
from flask.ext.restful import Resource

from jmilkfansblog.controllers.flask_restful import parsers
from jmilkfansblog.db.sqlalchemy.models import User


class AuthApi(Resource):
    """Restful api of Auth."""

    def post(self):
        """Can be execute when receive HTTP Method `POST`."""

        args = parsers.user_post_parser.parse_args()
        user = User.query.filter_by(username=args['username']).first()

        # Check the args['password'] whether as same as user.password.
        if user.check_password(args['password']):
            # serializer object will be saved the token period of time.
            serializer = Serializer(
                current_app.config['SECRET_KEY'],
                expires_in=600)
            return {'token': serializer.dumps({'id': user.id})}
        else:
            abort(401)
