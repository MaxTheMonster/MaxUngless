# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-22 07:15
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0004_auto_20161122_0705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateField(default=datetime.datetime(2016, 11, 22, 7, 15, 43, 550135)),
        ),
    ]
