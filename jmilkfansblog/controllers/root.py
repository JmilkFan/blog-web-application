"""Root(`/`) controller Pecan RESTful API."""

from pecan import rest
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan

from jmilkfansblog.api import expose
from jmilkfansblog.controllers.v1 import controller as v1_controller


class RootController(rest.RestController):

    v1 = v1_controller.V1Controller()

    # Route Controller decorator `expose`.
    @expose.expose(wtypes.text)
    def get(self):
        """Processing the GET `/`."""
        return "jmilkfansblog"
