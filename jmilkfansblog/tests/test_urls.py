import unittest

from jmilkfansblog import create_app
from jmilkfansblog.models import db


class TestURLs(unittest.TestCase):
    """Unit test for route functions."""

    def setUp(self):
        # Destroy the Flask-Admin and Flask-Result object after delete app object
        admin._views = []
        rest_api.resource = []

        app = create_app('jmilkfansblog.config.TestConfig')
        self.client = app.test_client()

        # Using Test app for db
        db.app = app
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

if __name__ == '__main__':
    unittest.main()
