import datetime
import tempfile
from os import path

from oslo_config import cfg
from oslo_log import log as logging

from celery.schedules import crontab


jmilkfansblog_default_opts = [
    cfg.StrOpt('host',
               default='localhost',
               help="Server ipaddress of jmilkfansblog."),

    cfg.IntOpt('server_port',
               default=8089,
               help="Server port of jmilkfansblog."),

    cfg.IntOpt('api_port',
               default=8080,
               help="API port of jmilkfansblog."),

    cfg.StrOpt('recaptcha_public_key',
               help="Google reCaptcha public key."),

    cfg.StrOpt('recaptcha_private_key',
               help="Google reCaptche private key.")]

flask_wtform_group = cfg.OptGroup(name='flask_wtform')
flask_wtform_secret_key_opt = cfg.StrOpt('secret_key',
                                         help="Flask-WTForm.")

flask_debugtoolbar_group = cfg.OptGroup(name='flask_debugtoolbar')
flask_debugtoolbar_opt = cfg.StrOpt('debug',
                                    default=False,
                                    help="Flask-DebugToolBar.")

flask_cache_group = cfg.OptGroup(name='flask_cache')
flask_cache_type_opt = cfg.StrOpt('cache_type',
                                  help="Flask-Cache.")

flask_assets_group = cfg.OptGroup(name='flask_assets')
flask_assets_debug_opt = cfg.BoolOpt('assets_debug',
                                     help="Flask-Assets.")

celery_group = cfg.OptGroup(name='celery')
celery_opts = [
    cfg.StrOpt('celery_result_backend',
               default='amqp://guest:guest@localhost:5672//',
               help="Celery result backend."),
    cfg.StrOpt('celery_broker_url',
               default='amqp://guest:guest@localhost:5672//',
               help="Celery broker url.")]

sqlalchemy_group = cfg.OptGroup(name='database')
sqlalchemy_opts =  [
    cfg.StrOpt('connection',
               help='SQLAlchemy.'),
    cfg.StrOpt('backend',
               help="Multi-Backend.")]

CONF = cfg.CONF
CONF.register_opts(jmilkfansblog_default_opts)

CONF.register_group(flask_wtform_group)
CONF.register_opt(flask_wtform_secret_key_opt, flask_wtform_group)

CONF.register_group(flask_debugtoolbar_group)
CONF.register_opt(flask_debugtoolbar_opt, flask_debugtoolbar_group)

CONF.register_group(flask_cache_group)
CONF.register_opt(flask_cache_type_opt, flask_cache_group)

CONF.register_group(flask_assets_group)
CONF.register_opt(flask_assets_debug_opt, flask_assets_group)

CONF.register_group(celery_group)
CONF.register_opts(celery_opts, celery_group)

CONF.register_group(sqlalchemy_group)
CONF.register_opts(sqlalchemy_opts, sqlalchemy_group)

CONFIG_FILE = path.join('etc', 'jmilkfansblog.conf')


LOG = logging.getLogger(__name__)
DOMAIN = "jmilkfansblog"
# Have to define the param `args(List)`,
# otherwise will be capture the CLI option when execute `python manage.py server`.
# oslo_config: (args if args is not None else sys.argv[1:])
CONF(args=[], project=DOMAIN, default_config_files=[CONFIG_FILE])
#logging.setup(CONF, DOMAIN)


class Config(object):
    """Base config class."""

    # WTForm secret key
    SECRET_KEY = CONF.flask_wtform.secret_key
    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = CONF.recaptcha_public_key
    RECAPTCHA_PRIVATE_KEY = CONF.recaptcha_private_key


class ProdConfig(Config):
    """Production config class."""

    DEBUG = CONF.flask_debugtoolbar.debug
    CACHE_TYPE = CONF.flask_cache.cache_type
    ASSETS_DEBUG = CONF.flask_assets.assets_debug
    CELERY_RESULT_BACKEND = CONF.celery.celery_result_backend
    CELERY_BROKER_URL = CONF.celery.celery_broker_url
    SQLALCHEMY_DATABASE_URI = CONF.database.connection

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
