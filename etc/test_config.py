from oslo_config import cfg


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

sqlalchemy_group = cfg.OptGroup(
    name='flask_sqlalchemy')

sqlalchemy_uri_opt = cfg.StrOpt('SQLALCHEMY_DATABASE_URI',
                                help='SQLAlchemy.')

CONF = cfg.CONF
CONF.register_opts(jmilkfansblog_default_opts)
CONF.register_group(sqlalchemy_group)
CONF.register_opt(sqlalchemy_uri_opt, sqlalchemy_group)

if __name__ == '__main__':
    CONF(default_config_files=['jmilkfansblog.conf'])
    print CONF.DEBUG
    print CONF.flask_sqlalchemy.SQLALCHEMY_DATABASE_URI
