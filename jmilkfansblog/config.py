import datetime
from celery.schedules import crontab


class Config(object):
    """Base config class."""
    # WTForm secret key
    SECRET_KEY = 'c8e6ff3e4687709ca10a1138a17cd397'
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = "6LdBbA0UAAAAAFfpWX5fubCe8wwMp4MrjOyNqFfO"
    RECAPTCHA_PRIVATE_KEY = "6LdBbA0UAAAAABzQiANZIyCAjc4Rg6JiuQkWx6pr"


class ProdConfig(Config):
    """Production config class."""

    # Setup Cache type config
    # CACHE_TYPE = 'simple'

    # Setup the config for redis
    CACHE_TYPE = 'redis'
    CACHE_REDIS_HOST = 'localhost'
    CACHE_REDIS_PORT = '6379'
    # FIXME(JmilkFan): Choise the password of Redis
    CACHE_REDIS_PASSWORD = 'password'
    CACHE_REDIS_DB = '0'


class DevConfig(Config):
    """Development config class."""

    # Flask-Assets's config
    ASSETS_DEBUG = True

    # Flask-Debug-Toolbar's config
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

    # MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/myblog?charset=utf8'

    # Setup Cache type config
    CACHE_TYPE = 'null'

    # Celery <--> RabbitMQ connection
    CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost:5672//"
    CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"

    # Timed Task configuation of celery task `weekly digest`
    CELERYBEAT_SCHEDULE = {
        'weekly-digest': {
            # Setup the celery task.
            'task': 'jmilkfansblog.tasks.digest',
            # Setup the time span.
            'schedule': crontab(day_of_week=6, hour='10')}}

    # FIXME(JmilkFan): Deploy the smtp server in local
    # Setup the config for Flask-Mail
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = '<username>'
    MAIL_PASSWORD = '<password>'
