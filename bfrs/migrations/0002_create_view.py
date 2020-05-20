# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-04-04 06:24
from __future__ import unicode_literals

from django.db import migrations
from django.core.management import call_command
from bfrs.utils import update_users, create_other_user


class Migration(migrations.Migration):

    def run_create_view(apps, schema_editor):
        """ from https://docs.djangoproject.com/en/1.10/topics/migrations/ """
        call_command('loaddata', 'districts.json')
        call_command('loaddata', 'enum.json')
        create_other_user()
        update_users()

    dependencies = [
        ('bfrs', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(run_create_view),
    ]
