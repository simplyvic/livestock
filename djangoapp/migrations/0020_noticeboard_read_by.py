# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-27 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0019_auto_20200727_0049'),
    ]

    operations = [
        migrations.AddField(
            model_name='noticeboard',
            name='read_by',
            field=models.TextField(blank=True, max_length=10000),
        ),
    ]
