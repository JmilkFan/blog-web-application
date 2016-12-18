from flask import request
from gzip import GzipFile
from io import BytesIO


class GZip(object):
    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        app.after_request(self.after_request)

    def after_request(self, response):
        """Compress data for response."""

        # Check the Browser whether can be receive the gzip encoding.
        # and check the response whether successfully.
        encoding = request.headers.get('Accept-Encoding', '')
        if 'gzip' not in encoding or not response.status_code in (200, 201):
            return response

        # Response can't be direct passthrough.
        response.direct_passthrough = False

        contents = BytesIO()

        # Compress the response in the memory.
        with GzipFile(
            mode='wb',
            compresslevel=5,
            fileobj=contents) as gzip_file:
            gzip_file.write(response.get_data())

        response.set_data(bytes(contents.getvalue()))

        response.headers['Content-Encoding'] = 'gzip'
        response.headers['Content-Lenght'] = response.content_length

        return response
