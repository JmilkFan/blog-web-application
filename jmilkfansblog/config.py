class Config(object):
    """Base config class."""
    # WTForm secret key
    SECRET_KEY = 'c8e6ff3e4687709ca10a1138a17cd397'
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = "6LfoHg0UAAAAAJLuSB2PQMqRyMgdcrHCQ9JgBicu"
    RECAPTCHA_PRIVATE_KEY = "6LfoHg0UAAAAAFmK_vQfswAFwnr06rF1Q1zCgBXF"

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/myblog?charset=utf8'
