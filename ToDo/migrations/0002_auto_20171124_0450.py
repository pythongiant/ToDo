# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-24 04:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ToDo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='ToDo',
            new_name='aToDo',
        ),
    ]
