# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-31 10:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("somno", "0015_auto_20180831_0939")]

    operations = [
        migrations.AddField(
            model_name="infusion",
            name="concentration",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="givendrug",
            name="datetime",
            field=models.DateTimeField(blank=True, null=True, verbose_name="Start"),
        ),
    ]