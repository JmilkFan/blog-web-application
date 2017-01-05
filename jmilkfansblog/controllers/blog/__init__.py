from uuid import uuid4
from os import path
from datetime import datetime

from oslo_log import log as logging

from flask import render_template, redirect, Blueprint, url_for, flash
from flask import session, abort, request
from flask.ext.login import login_required, current_user
from flask.ext.principal import Permission, UserNeed
from sqlalchemy import func

from jmilkfansblog.models import db, User, Post, Tag, Comment, posts_tags
from jmilkfansblog.forms import CommentForm, PostForm
from jmilkfansblog.extensions import poster_permission, admin_permission, cache


LOG = logging.getLogger(__name__)

blog_blueprint = Blueprint(
    'blog',
    __name__,
    # path.pardir ==> ../
    template_folder=path.join(path.pardir, path.pardir, 'templates', 'blog'),
    # Prefix of Route URL 
    url_prefix='/blog')


def make_cache_key(*args, **kwargs):
    """Dynamic creation the request url."""

    path = request.path
    args = str(hash(frozenset(request.args.items())))
    # lang = get_locale()
    # return (path + args + lang).encode('utf-8')
    return (path + args).encode('utf-8')


@cache.cached(timeout=7200, key_prefix='sidebar_data')
def sidebar_data():
    """Set the sidebar function."""

    # Get post of recent
    recent = db.session.query(Post).order_by(
            Post.publish_date.desc()
        ).limit(5).all()

    # Get the tags and sort by count of posts.
    top_tags = db.session.query(
            Tag, func.count(posts_tags.c.post_id).label('total')
        ).join(
            posts_tags
        ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags


# Use the Blueprint object to set the Route URL
# Register the view function into blueprint
@blog_blueprint.route('/')
@blog_blueprint.route('/<int:page>')
@cache.cached(timeout=60)
def home(page=1):
    """View function for home page"""

    posts = Post.query.order_by(
        Post.publish_date.desc()
    ).paginate(page, 10)

    recent, top_tags = sidebar_data()

    return render_template('home.html',
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@blog_blueprint.route('/post/<string:post_id>', methods=('GET', 'POST'))
@cache.cached(timeout=60, key_prefix=make_cache_key)
def post(post_id):
    """View function for post page"""

    LOG.info("Access view function `post` and access URL `/post/%s`", post_id)
    # Form object: `Comment`
    form = CommentForm()
    # form.validate_on_submit() will be true and return the
    # data object to form instance from user enter,
    # when the HTTP request is POST
    if form.validate_on_submit():
        new_comment = Comment()
        new_comment.name = form.name.data
        new_comment.text = form.text.data
        new_comment.date = datetime.now()
        new_comment.post_id = post_id
        db.session.add(new_comment)
        db.session.commit()

    post = Post.query.get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('post.html',
                           post=post,
                           tags=tags,
                           comments=comments,
                           form=form,
                           recent=recent,
                           top_tags=top_tags,
                           poster_permission=poster_permission,
                           admin_permission=admin_permission)


@blog_blueprint.route('/tag/<string:tag_name>')
def tag(tag_name):
    """View function for tag page"""

    tag = Tag.query.filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('tag.html',
                           tag=tag,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@blog_blueprint.route('/user/<string:username>')
def user(username):
    """View function for user page"""
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.order_by(Post.publish_date.desc()).all()
    recent, top_tags = sidebar_data()

    return render_template('user.html',
                           user=user,
                           posts=posts,
                           recent=recent,
                           top_tags=top_tags)


@blog_blueprint.route('/new', methods=['GET', 'POST'])
@login_required
def new_post():
    """View function for new_port."""

    form = PostForm()

    # Ensure the user logged in.
    # Flask-Login.current_user can be access current user.
    if not current_user:
        return redirect(url_for('main.login'))

    # Will be execute when click the submit in the create a new post page.
    if form.validate_on_submit():
        new_post = Post()
        new_post.title = form.title.data
        new_post.text = form.text.data
        new_post.publish_date = datetime.now()
        new_post.user = current_user

        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('blog.home'))

    return render_template('new_post.html',
                           form=form)


@blog_blueprint.route('/edit/<string:id>', methods=['GET', 'POST'])
@login_required
@admin_permission.require(http_exception=403)
def edit_post(id):
    """View function for edit_post."""

    post = Post.query.get_or_404(id)

    # Ensure the user logged in.
    if not current_user:
        return redirect(url_for('main.login'))

    # Only the post onwer can be edit this post.
    if current_user != post.user:
        return redirect(url_for('blog.post', post_id=id))

    # Admin can be edit the post.
    permission = Permission(UserNeed(post.user.id))
    if permission.can() or admin_permission.can():
        form = PostForm()

        #if current_user != post.user:
        #    abort(403)

        if form.validate_on_submit():
            post.title = form.title.data
            post.text = form.text.data
            post.publish_date = datetime.now()

            # Update the post
            db.session.add(post)
            db.session.commit()

            return redirect(url_for('blog.post', post_id=post.id))
    else:
        abort(403)

    # Still retain the original content, if validate is false.
    form.title.data = post.title
    form.text.data = post.text
    return render_template('edit_post.html', form=form, post=post)


# NOTE(Jmilk Fan): Use the Flask-Login's current_user object to replace
#                  g.current_user
# @blog_blueprint.before_request
def check_user():
    """Check the user whether logged in."""

    if 'username' in session:
        g.current_user = User.query.filter_by(
            username=session['username']).first()
    else:
        g.current_user = None


@blog_blueprint.errorhandler(404)
def page_not_found(error):
    """View function for user page not found"""
    return render_template('page_not_found.html'), 404
