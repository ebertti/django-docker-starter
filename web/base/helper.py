# coding: utf-8
import uuid

import base58
import logging

from django.shortcuts import resolve_url
from django.utils.http import urlencode

logger = logging.getLogger('debug')

def gerar_hash():
    h = base58.b58encode(uuid.uuid4().bytes)
    return h


def get_ip(request):
    ip = request.META['REMOTE_ADDR']  # dev development
    if 'HTTP_X_FORWARDED_FOR' in request.META:  # load balancer aws
        ip = request.META['HTTP_X_FORWARDED_FOR']

    return ip


def resolvedor_url_com_anchor(para, *args, **kwargs):
    anchor = kwargs.pop('anchor', None)
    qs = kwargs.pop('qs', None)

    url = resolve_url(para, *args, **kwargs)

    if qs:
        url += '?' + urlencode(qs)

    if anchor:
        url += '#' + anchor

    return url
