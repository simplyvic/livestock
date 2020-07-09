# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-23 12:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_auto_20200414_0542'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=30)),
                ('name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='DiseaseReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee', models.CharField(blank=True, max_length=30)),
                ('date', models.DateField(blank=True, null=True)),
                ('reporter_name', models.CharField(blank=True, max_length=30, null=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('month', models.DateField(blank=True)),
                ('year', models.DateField(blank=True)),
                ('localty_longitude', models.CharField(blank=True, max_length=30)),
                ('localty_latitude', models.CharField(blank=True, max_length=30)),
                ('owner_name', models.CharField(blank=True, max_length=30, null=True)),
                ('owner_contact_no', models.CharField(blank=True, max_length=30, null=True)),
                ('owner_nin_no', models.CharField(blank=True, max_length=30, null=True)),
                ('specie_sex', models.CharField(blank=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')], max_length=30, null=True)),
                ('specie_age', models.CharField(blank=True, max_length=30)),
                ('animalID', models.CharField(blank=True, max_length=30)),
                ('pet_name', models.CharField(blank=True, max_length=30)),
                ('animal_group_size', models.CharField(blank=True, max_length=30)),
                ('clinical_prognosis', models.CharField(blank=True, choices=[(b'Good', b'Good'), (b'Poor', b'Poor')], max_length=30, null=True)),
                ('notifiable_disease', models.BooleanField(default=False)),
                ('timestamp', models.DateField(auto_now_add=True)),
                ('owner_gender', models.CharField(blank=True, choices=[(b'Male', b'Male'), (b'Female', b'Female')], max_length=30, null=True)),
                ('notification_frequency', models.CharField(blank=True, choices=[(b'Immediate Frequecy', b'Immediate Frequecy'), (b'Weekly Frequecy', b'Weekly Frequecy'), (b'Bi-Weekly Frequecy', b'Bi-Weekly Frequecy'), (b'Monthly Frequecy', b'Monthly Frequecy')], max_length=30, null=True)),
                ('zoonosis', models.BooleanField(default=False)),
                ('noofcases', models.CharField(blank=True, max_length=30, null=True)),
                ('noofdeaths', models.CharField(blank=True, max_length=30, null=True)),
                ('nodestroyed', models.CharField(blank=True, max_length=30, null=True)),
                ('incedent_rate', models.CharField(blank=True, max_length=30, null=True)),
                ('motality_rate', models.CharField(blank=True, max_length=30, null=True)),
                ('moditity_rate', models.CharField(blank=True, max_length=30, null=True)),
                ('lab_sample_collected', models.BooleanField(default=False)),
                ('sample_type', models.CharField(blank=True, choices=[(b'Swabs', b'Swabs'), (b'LymphNode', b'LymphNode'), (b'Organ-kidney', b'Organ-Kidney'), (b'Organ-Lungs', b'Organ-Lungs'), (b'Organ-Intestine', b'Organ-Intestine'), (b'Organ-Heart', b'Organ-Heart'), (b'Organ-Trachea', b'Organ-Trachea'), (b'Organ-Esophagus', b'Organ-Esophagus'), (b'Organ-Brain', b'Organ-Brain')], max_length=30, null=True)),
                ('sample_ID', models.CharField(blank=True, max_length=30, null=True)),
                ('lab_test_applied', models.CharField(blank=True, choices=[(b'cELISA', b'cELISA'), (b'PCR', b'PCR'), (b'Realtime PCR', b'Realtime PCR'), (b'Cultures', b'Cultures'), (b'Haematology', b'Haematology'), (b'Smears', b'Smears'), (b'Parasitology', b'Parasitology'), (b'IFAT', b'IFAT')], max_length=30, null=True)),
                ('lab_test_results', models.CharField(blank=True, choices=[(b'Positive', b'Positive'), (b'Negative', b'Negative')], max_length=30, null=True)),
                ('export_to_CSV', models.BooleanField(default=False)),
                ('clinical_diagnosis', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.ClinicalDiagnosis')),
                ('control_measures', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.ControlMeasures')),
                ('disease_code', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.DiseaseCode')),
                ('localty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.Localty')),
                ('principal_signs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.PrincipalSign')),
                ('quarter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.Quarter')),
                ('species', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.Species')),
                ('species_breed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.SpeciesBreed')),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=30)),
                ('short_name', models.CharField(blank=True, max_length=30)),
                ('full_name', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='computer',
            name='operating_system',
        ),
        migrations.RemoveField(
            model_name='computerhistory',
            name='operating_system',
        ),
        migrations.DeleteModel(
            name='Computer',
        ),
        migrations.DeleteModel(
            name='ComputerHistory',
        ),
        migrations.DeleteModel(
            name='Operating_system',
        ),
        migrations.AddField(
            model_name='diseasereport',
            name='vaccination_history',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='djangoapp.VaccinationHistory'),
        ),
    ]