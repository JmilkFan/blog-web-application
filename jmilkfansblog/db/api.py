"""Support the multi-backend."""

from oslo_config import cfg
from oslo_db import concurrency as db_concurrency
from oslo_db import options as db_options


db_opts = []

CONF = cfg.CONF
CONF.register_opts(db_opts)
db_options.set_defaults(CONF)

_BACKEND_MAPPING = {'sqlalchemy', 'jmilkfansblog.db.sqlalchemy.api'}

TMPL = db_concurrency.TpoolDbapiWrapper(CONF,
                                        backend_mapping=_BACKEND_MAPPING)


def dispose_engine():
    """Force the engine to establish new connections."""
    return IMPL.dispose_engine()
