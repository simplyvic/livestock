# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clinical',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('employee', models.CharField(max_length=30, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('clinical_name', models.CharField(max_length=30, null=True, blank=True)),
                ('specie_sex', models.CharField(blank=True, max_length=30, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('owner_name', models.CharField(max_length=30, null=True, blank=True)),
                ('owner_contact_no', models.CharField(max_length=30, null=True, blank=True)),
                ('owner_gender', models.CharField(blank=True, max_length=30, null=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')])),
                ('localty_longitude', models.CharField(max_length=30, blank=True)),
                ('localty_latitude', models.CharField(max_length=30, blank=True)),
                ('animal_group_size', models.CharField(max_length=30, blank=True)),
                ('animalID', models.CharField(max_length=30, blank=True)),
                ('pet_name', models.CharField(max_length=30, blank=True)),
                ('animal_live_weight', models.CharField(max_length=30, verbose_name=b'Animal live weight (KG)', blank=True)),
                ('anamnesis', models.CharField(max_length=30, blank=True)),
                ('clinical_prognosis', models.CharField(blank=True, max_length=30, null=True, choices=[(b'Good', b'Good'), (b'Poor', b'Poor')])),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('aproved', models.BooleanField(default=False)),
                ('export_to_CSV', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ClinicalDiagnosis',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, blank=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ControlMeasures',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='General',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Localty',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('code', models.CharField(max_length=30, blank=True)),
                ('short_name', models.CharField(max_length=30, blank=True)),
                ('full_name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrincipalSign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SampleType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Species',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpeciesBreed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='clinical',
            name='clinical_diagnosis',
            field=models.ForeignKey(blank=True, to='djangoapp.ClinicalDiagnosis', null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='localty',
            field=models.ForeignKey(blank=True, to='djangoapp.Localty', null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='principal_signs',
            field=models.ForeignKey(blank=True, to='djangoapp.PrincipalSign', null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='quarter',
            field=models.ForeignKey(blank=True, to='djangoapp.Quarter', null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='region',
            field=models.ForeignKey(blank=True, to='djangoapp.Region', null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='species',
            field=models.ForeignKey(blank=True, to='djangoapp.Species', null=True),
        ),
        migrations.AddField(
            model_name='clinical',
            name='species_breed',
            field=models.ForeignKey(blank=True, to='djangoapp.SpeciesBreed', null=True),
        ),
    ]
