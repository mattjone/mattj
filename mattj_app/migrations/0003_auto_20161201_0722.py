# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-01 07:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mattj_app', '0002_auto_20161130_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
