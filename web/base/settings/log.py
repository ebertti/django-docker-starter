import logging
from django.conf import settings

class PseudoTTY(object):
    """This allows a a fake tty which will allow PyCharm to always say its a tty"""
    def __init__(self, underlying):
        """Define my underlying class"""
        self.__underlying = underlying

    def __getattr__(self, name):
        """Pass me along to my parent"""
        return getattr(self.__underlying, name)

    def isatty(self):
        """Force this to always be True"""
        return True


class NotStaticFile(logging.Filter):
    def filter(self, record):
        if hasattr(record, 'args') and len(record.args) > 2:
            if settings.STATIC_URL in record.args[0] and record.args[1] in ('200', '304'):
                return False
        return True