# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-06 15:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0012_auto_20200706_1540'),
    ]

    operations = [
        migrations.RenameField(
            model_name='abattoir',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='diseasereport',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='lab',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='locality',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='permits',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='production',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='transportfleet',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='vaccination',
            old_name='approve',
            new_name='approve_one',
        ),
        migrations.RenameField(
            model_name='vetinfraindustry',
            old_name='approve',
            new_name='approve_one',
        ),
    ]
