# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='gm',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
