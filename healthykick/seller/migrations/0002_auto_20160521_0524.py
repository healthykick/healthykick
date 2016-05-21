# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-21 05:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='seller',
            old_name='firstname',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='seller',
            name='lastname',
        ),
        migrations.AlterField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 21, 5, 24, 27, 78786), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 5, 21, 5, 24, 27, 78850), verbose_name='Updated Date'),
        ),
    ]