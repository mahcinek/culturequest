# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 20:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20160415_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='content',
        ),
    ]
