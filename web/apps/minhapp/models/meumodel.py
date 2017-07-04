from django.db import models

from base.choices import MeusChoices
from base.models.mixin import BaseModelMixin
from base.models.queryset import BaseQuerySetMixin


class MeuModelQuerySet(BaseQuerySetMixin, models.QuerySet):
    pass



# nao esquece do import no __init__ do models

class MeuModel(BaseModelMixin, models.Model):
    nome = models.CharField(max_length=50)
    opcao = models.CharField(max_length=20, choices=MeusChoices.choices)

    objects  = MeuModelQuerySet.as_manager()