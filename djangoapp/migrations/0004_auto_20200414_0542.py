# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0003_auto_20200414_0518'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinical',
            old_name='aproved',
            new_name='approve',
        ),
    ]
