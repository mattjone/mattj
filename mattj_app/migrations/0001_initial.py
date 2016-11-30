# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 01:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exp_type', models.CharField(choices=[('education', 'Education'), ('professional', 'Professional')], default='professional', max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('employer', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=1000)),
            ],
        ),
    ]