from flask import Blueprint, Markup
from flask import flash, redirect, url_for, session, render_template


class Youku(object):
    """Flask-Youku extents."""

    def __init__(self, app=None, **kwargs):
        """Init Flask-Youku's instance via app object"""        
        if app:
            self.init_app(app)

    def init_app(self, app):
        """Init Flask-Youku's instance via app object"""        

        self.register_blueprint(app)
        # Create the Jinja function `youku`
        app.add_template_global(youku)

    def register_blueprint(self, app):
        """Register the youku blueprint into app object."""
        module = Blueprint(
            'youku',
            __name__,
            template_folder='templates')
        app.register_blueprint(module)
        return module


class Video(object):
    """Receive the youku_id to rendering the video.html"""

    def __init__(self, video_id, cls='youku'):
        self.video_id = video_id
        self.cls = cls

    def render(self, *args, **kwargs):
        return render_template(*args, **kwargs)

    @property
    def html(self):
        """Tag the HTML as security string."""

        return Markup(
            self.render('youku/video.html', video=self))


def youku(*args, **kwargs):
    """Define the Jinja function."""

    video = Video(*args, **kwargs)
    return video.html
