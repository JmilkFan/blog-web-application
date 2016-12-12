class Config(object):
    """Base config class."""
    # WTForm secret key
    SECRET_KEY = 'c8e6ff3e4687709ca10a1138a17cd397'
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = "6LdBbA0UAAAAAFfpWX5fubCe8wwMp4MrjOyNqFfO"
    RECAPTCHA_PRIVATE_KEY = "6LdBbA0UAAAAABzQiANZIyCAjc4Rg6JiuQkWx6pr"

class ProdConfig(Config):
    """Production config class."""
    pass

class DevConfig(Config):
    """Development config class."""
    DEBUG = True
    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/myblog?charset=utf8'
    # Celery <--> RabbitMQ connection
    CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost:5672//"
    CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
