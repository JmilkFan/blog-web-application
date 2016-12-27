class ViewBuilder(object):
    def show(self, post, brief=False):
        trimmed = dict(id=post.get('id'),
                       author=post.get('author'),
                       title=post.get('title'),
                       text=post.get('text'),
                       tags=post.get('tags'),
                       publish_date=post.get('publish_date'))
        return trimmed if brief else dict(post=trimmed)

    def index(self, posts):
        post_list = [self.show(post, brief=True) for post in posts]
        return dict(posts=post_list)
