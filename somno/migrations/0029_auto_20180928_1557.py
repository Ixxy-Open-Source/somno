# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-09-28 15:57
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import opal.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('opal', '0035_auto_20180806_1150'),
        ('somno', '0028_auto_20180928_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='AnaestheticProcedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(blank=True, null=True)),
                ('consistency_token', models.CharField(max_length=8)),
                ('Number_Of_Attempts', models.FloatField(blank=True, null=True)),
                ('Depth_Of_Space', models.FloatField(blank=True, null=True)),
                ('Catheter_Left_In', models.FloatField(blank=True, null=True)),
                ('Drug_Concentration', models.FloatField(blank=True, null=True)),
                ('Drug_Dose', models.FloatField(blank=True, null=True)),
                ('Procedure_Note', models.TextField(blank=True, null=True)),
                ('Time_Done', models.DateTimeField(blank=True, null=True)),
                ('Device_Used_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Technique_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Ultrasound_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Procedure_Name_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Procedure_Type_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Body_Site_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Drug_Used_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
                ('Sterility_ft', models.CharField(blank=True, default=b'', max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(opal.models.UpdatesFromDictMixin, opal.models.ToDictMixin, models.Model),
        ),
        migrations.CreateModel(
            name='BodySite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProcedureDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProcedureName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProcedureSterility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProcedureTechnique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProcedureType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='ProcedureUltrasound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'abstract': False,
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Body_Site_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.BodySite'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Device_Used_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ProcedureDevice'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Drug_Used_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.AnaestheticDrug'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Procedure_Name_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ProcedureName'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Procedure_Type_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ProcedureType'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Sterility_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ProcedureSterility'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Technique_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ProcedureTechnique'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='Ultrasound_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='somno.ProcedureUltrasound'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_somno_anaestheticprocedure_subrecords', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='episode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='opal.Episode'),
        ),
        migrations.AddField(
            model_name='anaestheticprocedure',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_somno_anaestheticprocedure_subrecords', to=settings.AUTH_USER_MODEL),
        ),
    ]
