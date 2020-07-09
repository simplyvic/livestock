# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0002_auto_20200414_0445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clinical',
            name='aproved',
            field=models.CharField(blank=True, max_length=30, null=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')]),
        ),
    ]
