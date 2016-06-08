# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0002_auto_20160521_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 3, 52, 32, 6549), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 3, 52, 32, 6661), verbose_name='Updated Date'),
        ),
        migrations.AlterField(
            model_name='sellerdetail',
            name='mobile_number',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
