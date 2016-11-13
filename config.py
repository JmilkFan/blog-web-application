class Config(object):
    """Base config class."""
    pass

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:fanguiju@127.0.0.1:3356/myblog'
