# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-25 16:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('somno', '0006_auto_20180725_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infusion',
            name='rate',
            field=models.CharField(blank=True, default='', max_length=255),
        ),
    ]
