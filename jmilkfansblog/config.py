import datetime
import tempfile
from os import path

from oslo_config import cfg

from celery.schedules import crontab


jmilkfansblog_default_opts = [
    cfg.BoolOpt('DEBUG',
                default=True,
                help="Close the debug."),

    cfg.StrOpt('SECRET_KEY',
               help="WTForm secret key."),

    cfg.StrOpt('RECAPTCHA_PUBLIC_KEY',
               help="Google reCaptcha public key."),

    cfg.StrOpt('RECAPTCHA_PRIVATE_KEY',
               help="Google reCaptche private key."),

    cfg.StrOpt('CELERY_RESULT_BACKEND',
               help='Celery Backend.'),

    cfg.StrOpt('CELERY_BROKER_URL',
               help='Celery Broker.'),

    cfg.StrOpt('CACHE_TYPE',
               default='null',
               help='Flask-Cache.'),

    cfg.BoolOpt('ASSETS_DEBUG',
                default=True,
                help='Flask-Assets.')]

sqlalchemy_group = cfg.OptGroup(name='flask_sqlalchemy')

sqlalchemy_uri_opt = cfg.StrOpt('SQLALCHEMY_DATABASE_URI',
                                help='SQLAlchemy.')

CONF = cfg.CONF
CONF.register_opts(jmilkfansblog_default_opts)
CONF.register_group(sqlalchemy_group)
CONF.register_opt(sqlalchemy_uri_opt, sqlalchemy_group)

CONFIG_FILE = path.join('etc', 'jmilkfansblog.conf')

# Have to define the param `args(List)`, 
# otherwise will be capture the CLI option when execute `python manage.py server`.
# oslo_config: (args if args is not None else sys.argv[1:])
CONF(args=[], default_config_files=[CONFIG_FILE])


class Config(object):
    """Base config class."""

    # WTForm secret key
    SECRET_KEY = CONF.SECRET_KEY
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = CONF.RECAPTCHA_PUBLIC_KEY
    RECAPTCHA_PRIVATE_KEY = CONF.RECAPTCHA_PRIVATE_KEY


class ProdConfig(Config):
    """Production config class."""

    DEBUG = CONF.DEBUG
    CACHE_TYPE = CONF.CACHE_TYPE
    ASSETS_DEBUG = CONF.ASSETS_DEBUG
    CELERY_RESULT_BACKEND = CONF.CELERY_RESULT_BACKEND
    CELERY_BROKER_URL = CONF.CELERY_BROKER_URL
    SQLALCHEMY_DATABASE_URI = CONF.flask_sqlalchemy.SQLALCHEMY_DATABASE_URI

    #### Setup the config for redis
    # CACHE_TYPE = 'redis'
    # CACHE_REDIS_HOST = 'localhost'
    # CACHE_REDIS_PORT = '6379'
    # FIXME(JmilkFan): Choise the password of Redis
    # CACHE_REDIS_PASSWORD = 'password'
    # CACHE_REDIS_DB = '0'


class DevConfig(Config):
    """Development config class."""

    #### Flask-Assets's config
    # Can not compress the CSS/JS on Dev environment.
    ASSETS_DEBUG = True

    #### Flask-Debug-Toolbar's config
    DEBUG = True
    # No intercept redirects
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    # Enable the profiler on all requests
    DEBUG_TB_PROFILER_ENABLED = True

    #### Flask-SQLAlchemy's config MySQL connection
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/myblog?charset=utf8'

    #### Flask-Cache's config
    CACHE_TYPE = 'null'

    #### Celery's config: Celery <--> RabbitMQ <--> APP connection
    CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost:5672//"
    CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
    # Timed Task configuation of celery task `weekly digest`
    # CELERYBEAT_SCHEDULE = {
    #     'weekly-digest': {
    #         # Setup the celery task.
    #         'task': 'jmilkfansblog.tasks.digest',
    #         # Setup the time span.
    #         'schedule': crontab(day_of_week=6, hour='10')}}

    #### Flask-Mail's Config
    # FIXME(JmilkFan): Deploy the smtp server in local
    MAIL_SERVER = 'localhost'
    MAIL_PORT = 25
    MAIL_USERNAME = '<username>'
    MAIL_PASSWORD = '<password>'


class TestConfig(Config):

    # Using the temp file to test.
    # Can't effect the data of DevENV
    db_file = tempfile.NamedTemporaryFile()
    # Close the CSRF check for WTForm.
    WTF_CSRF_ENABLED = False

    DEBUG = True
    DEBUG_TB_ENABLED = False

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:fanguiju@127.0.0.1:3306/myblog?charset=utf8'

    CACHE_TYPE = 'null'

    CELERY_RESULT_BACKEND = "amqp://guest:guest@localhost:5672//"
    CELERY_BROKER_URL = "amqp://guest:guest@localhost:5672//"
