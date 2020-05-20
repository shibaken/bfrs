# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-03-15 02:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bfrs', '0007_auto_20180314_0805'),
    ]

    operations = [
        migrations.CreateModel(
            name='BushfireProperty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=32, verbose_name=b'Property Name')),
                ('value', models.TextField(blank=True, null=True, verbose_name=b'Property Value')),
                ('bushfire', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='bfrs.Bushfire')),
            ],
        ),
        migrations.CreateModel(
            name='BushfirePropertySnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, max_length=32, verbose_name=b'Property Name')),
                ('value', models.TextField(blank=True, null=True, verbose_name=b'Property Value')),
                ('snapshot_type', models.PositiveSmallIntegerField(choices=[(1, b'Initial'), (2, b'Final')])),
                ('snapshot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties_snapshot', to='bfrs.BushfireSnapshot')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='bushfirepropertysnapshot',
            unique_together=set([('snapshot', 'snapshot_type', 'name')]),
        ),
        migrations.AlterUniqueTogether(
            name='bushfireproperty',
            unique_together=set([('bushfire', 'name')]),
        ),
    ]
