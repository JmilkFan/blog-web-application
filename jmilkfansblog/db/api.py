"""Support the multi-backend."""

from oslo_config import cfg
from oslo_db import concurrency as db_concurrency
from oslo_db import options as db_options
from oslo_db import api as db_api


db_opts = []

CONF = cfg.CONF
# Load the config option from etc.jmilkfansblog
CONF.register_opts(db_opts)
db_options.set_defaults(CONF)

_BACKEND_MAPPING = {'sqlalchemy': 'jmilkfansblog.db.sqlalchemy.api'}

# IMPL = db_api.DBAPI.from_config(CONF, backend_mapping=_BACKEND_MAPPING)
# NOTE(Fan Guiju): CONF.database.connection == None
IMPL = db_concurrency.TpoolDbapiWrapper(CONF,
                                        backend_mapping=_BACKEND_MAPPING)


def dispose_engine():
    """Force the engine to establish new connections."""
    return IMPL.dispose_engine()


def user_get_all():
    return IMPL.user_get_all()


def post_get_all():
    return IMPL.post_get_all()
