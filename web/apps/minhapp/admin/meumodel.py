from django.contrib import admin
from django.contrib.admin.options import BaseModelAdmin


class MeuModelAdmin(BaseModelAdmin, admin.ModelAdmin):
    pass