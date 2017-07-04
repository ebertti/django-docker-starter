from django.contrib import admin

from base.admin.mixin import BaseAdminMixin


class MeuModelAdmin(BaseAdminMixin, admin.ModelAdmin):
    pass