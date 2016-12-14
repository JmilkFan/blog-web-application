from flask.ext.admin import BaseView, expose
from flask.ext.admin.contrib.fileadmin import FileAdmin
from flask.ext.admin.contrib.sqla import ModelView

from jmilkfansblog.forms import CKTextAreaField


class CustomView(BaseView):
    """View function of Flask-Admin for Custom page."""

    @expose('/')
    def index(self):
        return self.render('admin/custom.html')

    @expose('/second_page')
    def second_page(self):
        return self.render('admin/second_page.html')


class CustomModelView(ModelView):
    """View function of Flask-Admin for Models page."""

    pass


class PostView(CustomModelView):
    """View function of Flask-Admin for Post create/edit Page includedin Models page"""

    form_overrides = dict(text=CKTextAreaField)

    column_searchable_list = ('text', 'title')
    column_filters = ('publish_date',)

    create_template = 'admin/post_edit.html'
    edit_template = 'admin/post_edit.html'


class CustomFileAdmin(FileAdmin):
    pass
