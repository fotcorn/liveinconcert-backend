# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-30 17:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liveinconcert', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='artistrating',
            unique_together=set([('user', 'artist')]),
        ),
    ]
