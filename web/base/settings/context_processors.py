import os

from django.conf import settings
import raven
from django.utils.functional import SimpleLazyObject

from base.indicadores import get_indicadores

VERSAO = os.environ.get('VERSAO', False)
if not VERSAO:
    try:
        VERSAO = raven.fetch_git_sha(settings.ROOT_DIR)[:7]
    except:
        VERSAO = "LOCAL"


def ambiente(request):
    return {
        'STAGE': settings.STAGE,
        'VERSAO': VERSAO
    }