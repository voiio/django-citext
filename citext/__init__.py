"""PostgreSQL CIText integration for Django."""

from . import _version
from .fields import *  # noqa
from .operations import *  # noqa

__version__ = _version.version
VERSION = _version.version_tuple
