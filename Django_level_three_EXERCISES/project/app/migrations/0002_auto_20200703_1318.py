# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2020-07-03 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='firstName',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='lastName',
            field=models.CharField(max_length=20),
        ),
    ]