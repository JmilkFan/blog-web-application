from oslo_config import cfg
from oslo_log import log as logging


DEFAULT_OPTS = [

    cfg.StrOpt('host',
               default='localhost',
               help="Server ipaddress of jmilkfansblog."),

    cfg.IntOpt('server_port',
               default=8088,
               help="Server port of jmilkfansblog."),

    cfg.IntOpt('api_port',
               default=8080,
               help="API port of jmilkfansblog."),

    cfg.StrOpt('recaptcha_public_key',
               help="Google reCaptcha public key."),

    cfg.StrOpt('recaptcha_private_key',
               help="Google reCaptche private key."),
]

DATABASE_GROUP = cfg.OptGroup(name='database')
DATABASE_OPTS = [

    cfg.StrOpt('connection',
               help='SQLAlchemy connection.'),

    cfg.StrOpt('backend',
               default='mysql',
               help="Multi-Backend.")
]

WTF_GROUP = cfg.OptGroup(name='flask_wtform')
WTF_OPTS = [

    cfg.StrOpt('SECRET_KEY',
               help="Flask-WTF secret key."),

    cfg.BoolOpt('WTF_CSRF_ENABLED',
                default=False,
                help="CSRF check for Flask-WTF."),
]

DEBUGTOOLBAR_GROUP = cfg.OptGroup(name='flask_debugtoolbar')
DEBUGTOOLBAR_OPTS = [

    cfg.BoolOpt('DEBUG_TB_INTERCEPT_REDIRECTS',
                default=False,
                help="Intercept redirects."),

    cfg.BoolOpt('DEBUG_TB_PROFILER_ENABLED',
                default=True,
                help="Profiler on all requests."),

]

ASSETS_GROUP = cfg.OptGroup(name='flask_assets')
ASSETS_OPTS = [

    cfg.BoolOpt('ASSETS_DEBUG',
                default=True,
                help="Compress the CSS/JS file to implements web page loading"
                     "speed."),

]

CACHE_GROUP = cfg.OptGroup(name='flask_cache')
CACHE_OPTS = [

    cfg.StrOpt('CACHE_TYPE',
               default='null',
               help="Flask-Cache type."),

]

CELERY_GROUP = cfg.OptGroup(name='celery')
CELERY_OPTS = [

    cfg.StrOpt('CELERY_RESULT_BACKEND',
               default='amqp://guest:guest@localhost:5672//',
               help="Celery result backend."),

    cfg.StrOpt('CELERY_BROKER_URL',
               default='amqp://guest:guest@localhost:5672//',
               help="Celery broker url."),

]

CONF = cfg.CONF
DOMAIN = 'jmilkfansblog'

logging.register_options(CONF)
logging.setup(CONF, DOMAIN)

# Register the options index.
CONF.register_opts(DEFAULT_OPTS)

CONF.register_group(DATABASE_GROUP)
CONF.register_opts(DATABASE_OPTS, DATABASE_GROUP)

CONF.register_group(WTF_GROUP)
CONF.register_opts(WTF_OPTS, WTF_GROUP)

CONF.register_group(DEBUGTOOLBAR_GROUP)
CONF.register_opts(DEBUGTOOLBAR_OPTS, DEBUGTOOLBAR_GROUP)

CONF.register_group(ASSETS_GROUP)
CONF.register_opts(ASSETS_OPTS, ASSETS_GROUP)

CONF.register_group(CACHE_GROUP)
CONF.register_opts(CACHE_OPTS, CACHE_GROUP)

CONF.register_group(CELERY_GROUP)
CONF.register_opts(CELERY_OPTS, CELERY_GROUP)

# Parse the options
CONF(args=[], project=DOMAIN,
     default_config_files=['etc/jmilkfansblog.conf'])


class Config(object):
    """Application config."""

    DEBUG = CONF.debug

    # reCAPTCHA Public key and Private key
    RECAPTCHA_PUBLIC_KEY = CONF.recaptcha_public_key
    RECAPTCHA_PRIVATE_KEY = CONF.recaptcha_private_key

    # Flask-SQLAlchemy's configuration
    SQLALCHEMY_DATABASE_URI = CONF.database.connection

    # Flask-WTF's configuration
    # secret key
    SECRET_KEY = CONF.flask_wtform.SECRET_KEY
    # NOTE(JmilkFan): Should not set 'False' when run the unit testting.
    WTF_CSRF_ENABLED = CONF.flask_wtform.WTF_CSRF_ENABLED

    # Flask-debugtoolbar's configuration
    # No intercept redirects
    DEBUG_TB_INTERCEPT_REDIRECTS = \
        CONF.flask_debugtoolbar.DEBUG_TB_INTERCEPT_REDIRECTS
    # Enable the profiler on all requests
    DEBUG_TB_PROFILER_ENABLED = \
        CONF.flask_debugtoolbar.DEBUG_TB_PROFILER_ENABLED

    # Flask-Assets's configuration
    # NOTE(JmilkFan): Should not compress the CSS/JS when development stage
    ASSETS_DEBUG = CONF.flask_assets.ASSETS_DEBUG

    # Flask-Cache's configuration
    # NOTE(JmilkFan): Should be set 'null' when development stage
    CACHE_TYPE = CONF.flask_cache.CACHE_TYPE

    # Celery asynchronous task configuration
    # Celery <--> RabbitMQ <--> APP connection
    CELERY_RESULT_BACKEND = CONF.celery.CELERY_RESULT_BACKEND
    CELERY_BROKER_URL = CONF.celery.CELERY_BROKER_URL
    # Timed Task configuation of celery task `weekly digest`
    # CELERYBEAT_SCHEDULE = {
    #     'weekly-digest': {
    #         # Setup the celery task.
    #         'task': 'jmilkfansblog.tasks.digest',
    #         # Setup the time span.
    #         'schedule': crontab(day_of_week=6, hour='10')}}
