# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-08-31 11:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('somno', '0018_auto_20180831_1108'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anaestheticnote',
            old_name='title',
            new_name='name',
        ),
    ]
