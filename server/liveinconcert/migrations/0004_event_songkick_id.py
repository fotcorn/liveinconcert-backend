# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-13 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liveinconcert', '0003_auto_20160213_1407'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='songkick_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Songkick ID'),
        ),
    ]
