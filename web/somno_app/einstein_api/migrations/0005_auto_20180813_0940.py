# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-13 09:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('einstein_api', '0004_auto_20180806_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pairing',
            name='subscription_id',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
