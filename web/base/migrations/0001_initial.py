# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-03 17:01
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import migrations
from django.conf import settings


def forward(apps, schema_editor):

    if not User.objects.filter(username='admin').exists():
        user = User.objects.create_superuser('admin', 'admin@admin.com', 'teste')


def reverte(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RunPython(forward, reverte),
    ]