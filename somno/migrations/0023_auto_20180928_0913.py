# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-28 09:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somno', '0022_merge_20180831_1212'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='diagnosis',
            options={'verbose_name': 'Diagnosis / Issues', 'verbose_name_plural': 'Diagnoses'},
        ),
        migrations.AlterModelOptions(
            name='investigation',
            options={'verbose_name': 'Investigations'},
        ),
        migrations.AlterModelOptions(
            name='pastmedicalhistory',
            options={'verbose_name': 'PMH', 'verbose_name_plural': 'Past medical histories'},
        ),
        migrations.RenameField(
            model_name='anaestheticassesment',
            old_name='ASA_fk',
            new_name='asa_fk',
        ),
        migrations.RenameField(
            model_name='anaestheticassesment',
            old_name='ASA_ft',
            new_name='asa_ft',
        ),
        migrations.RenameField(
            model_name='anaestheticassesment',
            old_name='Assessment',
            new_name='assessment',
        ),
        migrations.RenameField(
            model_name='anaestheticassesment',
            old_name='Frailty_fk',
            new_name='frailty_fk',
        ),
        migrations.RenameField(
            model_name='anaestheticassesment',
            old_name='Frailty_ft',
            new_name='frailty_ft',
        ),
        migrations.RenameField(
            model_name='anaestheticassesment',
            old_name='TimeSeen',
            new_name='time_seen',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='ExerciseTolerance',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='FastingStatus',
        ),
        migrations.RemoveField(
            model_name='anaestheticassesment',
            name='SmokingStatus',
        ),
        migrations.AddField(
            model_name='anaestheticassesment',
            name='exercise_tolerance',
            field=models.TextField(blank=True, null=True, verbose_name='Exercise tolerance'),
        ),
        migrations.AddField(
            model_name='anaestheticassesment',
            name='fasting_status',
            field=models.TextField(blank=True, null=True, verbose_name='Fasting status'),
        ),
        migrations.AddField(
            model_name='anaestheticassesment',
            name='smoking_status',
            field=models.TextField(blank=True, null=True, verbose_name='Smoking status'),
        ),
    ]
