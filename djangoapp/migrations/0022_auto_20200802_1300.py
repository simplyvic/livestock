# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-02 13:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0021_auto_20200727_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinical',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='diseasereport',
            name='date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
