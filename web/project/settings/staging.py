from __future__ import absolute_import, unicode_literals
import os

os.environ.setdefault("STAGE", "staging")

from .base import *



try:
    from .local import *
except ImportError:
    pass
