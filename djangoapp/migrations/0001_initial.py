# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Computer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('computer_name', models.CharField(max_length=30, blank=True)),
                ('IP_address', models.CharField(max_length=30, blank=True)),
                ('MAC_address', models.CharField(max_length=30, blank=True)),
                ('users_name', models.CharField(max_length=30, blank=True)),
                ('location', models.CharField(max_length=30, blank=True)),
                ('purchase_date', models.DateField(null=True, verbose_name=b'Purchase Date(mm/dd/2019)', blank=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ComputerHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('computer_name', models.CharField(max_length=30, blank=True)),
                ('IP_address', models.CharField(max_length=30, blank=True)),
                ('MAC_address', models.CharField(max_length=30, blank=True)),
                ('users_name', models.CharField(max_length=30, blank=True)),
                ('location', models.CharField(max_length=30, blank=True)),
                ('purchase_date', models.DateField(null=True, verbose_name=b'Purchase Date(mm/dd/2019)', blank=True)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Operating_system',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operating_system', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='computerhistory',
            name='operating_system',
            field=models.ForeignKey(blank=True, to='djangoapp.Operating_system', null=True),
        ),
        migrations.AddField(
            model_name='computer',
            name='operating_system',
            field=models.ForeignKey(blank=True, to='djangoapp.Operating_system', null=True),
        ),
    ]
