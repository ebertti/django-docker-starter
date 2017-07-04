from django.contrib.admin import sites

from .meumodel import MeuModelAdmin
from .. import models

sites.site.register(MeuModel, MeuModelAdmin)