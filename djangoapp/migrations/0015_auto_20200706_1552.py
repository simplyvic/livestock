# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-06 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0014_auto_20200706_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='abattoir',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='diseasereport',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='lab',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='locality',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='permits',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='production',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='transportfleet',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vaccination',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='vetinfraindustry',
            name='approve_two',
            field=models.CharField(blank=True, choices=[(b'Approve', b'Approve'), (b'Disapprove', b'Disapprove')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='abattoir',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='abattoir',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diseasereport',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='diseasereport',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lab',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locality',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='locality',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transportfleet',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='transportfleet',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vaccination',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vaccination',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vetinfraindustry',
            name='month',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vetinfraindustry',
            name='year',
            field=models.DateField(blank=True, null=True),
        ),
    ]
