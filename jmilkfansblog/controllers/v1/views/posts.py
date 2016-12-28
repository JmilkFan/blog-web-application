class ViewBuilder(object):
    def show(self, post, brief=False):
        trimmed = dict(id=post.id,
                       title=post.title,
                       text=post.text,
                       publish_date=post.publish_date,
                       user_id=post.user_id)
        return trimmed if brief else dict(post=trimmed)

    def index(self, posts):
        post_list = [self.show(post, brief=True) for post in posts]
        return dict(posts=post_list)
