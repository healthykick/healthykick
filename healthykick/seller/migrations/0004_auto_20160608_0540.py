# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0003_auto_20160608_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankdetail',
            name='bank_account_number',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='seller',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 5, 40, 37, 855285), verbose_name='Created Date'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 8, 5, 40, 37, 855345), verbose_name='Updated Date'),
        ),
    ]
