import random
import datetime
from uuid import uuid4

from jmilkfansblog.models import db, User, Post, Role, BrowseVolume

admin_role = Role(id=str(uuid4()), name='admin')
poster_role = Role(id=str(uuid4()), name='poster')
default_role = Role(id=str(uuid4()), name='default')

browse_volume = BrowseVolume(id=str(uuid4()))

db.session.add(default_role)
db.session.add(browse_volume)
db.session.commit()

admin_user = User(id=str(uuid4()), username='jmilkfan', password='fanguiju2016.com')
admin_user.roles = [admin_role, poster_role, default_role]

db.session.add(admin_user)
db.session.commit()
