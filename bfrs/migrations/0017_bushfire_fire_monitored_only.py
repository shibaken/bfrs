# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2017-05-22 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0016_bushfire_prescribed_burn_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='bushfire',
            name='fire_monitored_only',
            field=models.BooleanField(default=False),
        ),
    ]
