class Config(object):
    """Base config class."""
    SECRET_KEY = 'c8e6ff3e4687709ca10a1138a17cd397'

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/myblog?charset=utf8'
