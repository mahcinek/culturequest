# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 19:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_gm_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='gm',
            name='nick',
            field=models.CharField(default='', max_length=30),
        ),
    ]