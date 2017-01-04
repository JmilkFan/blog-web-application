"""Root(`/`) controller Pecan RESTful API."""

import pecan
from pecan import rest 
from wsme import types as wtypes
import wsmeext.pecan as wsme_pecan

from jmilkfansblog.api.expose import expose as wsexpose
from jmilkfansblog.controllers import v1 as v1_controller


class Root(wtypes.Base):

    name = wtypes.text
    """The name of the API"""

    description = wtypes.text
    """Some information about this API"""

    @staticmethod
    def convert():
        root = Root()
        root.name = "JmilkFan's Blog API"
        root.description = "JmilkFan's Blog with Python-Flask"
        return root


class RootController(rest.RestController):

    _versions = ['v1']
    """All supported API versions"""

    _default_version = 'v1'
    """The default API version"""

    v1 = v1_controller.Controller()

    # Route Controller decorator `expose`.
    @wsexpose(Root)
    def get(self):
        """Processing the GET `/`."""
        return Root.convert()
