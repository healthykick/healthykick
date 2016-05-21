# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-05-21 05:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=255)),
                ('bank_account_number', models.IntegerField()),
                ('ifsc_code', models.CharField(max_length=20)),
                ('bank_name', models.CharField(max_length=255)),
                ('bank_branch', models.CharField(max_length=255)),
                ('bank_state', models.CharField(max_length=255)),
                ('bank_city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='BussinessDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bussiness_name', models.CharField(max_length=255)),
                ('pan_number', models.IntegerField()),
                ('tin_number', models.IntegerField()),
                ('tan_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Catagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory_name', models.CharField(max_length=255)),
                ('catagory_alias', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('firstname', models.CharField(blank=True, max_length=255)),
                ('lastname', models.CharField(blank=True, max_length=255)),
                ('active', models.NullBooleanField()),
                ('created_at', models.DateTimeField(default=datetime.datetime(2016, 5, 21, 5, 5, 58, 240424), verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2016, 5, 21, 5, 5, 58, 240482), verbose_name='Updated Date')),
            ],
        ),
        migrations.CreateModel(
            name='SellerCatagory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Catagory')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='SellerDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_number', models.IntegerField(null=True)),
                ('address', models.TextField(null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('zip', models.IntegerField(null=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='SellerSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickup_address', models.TextField(null=True)),
                ('city', models.CharField(max_length=255, null=True)),
                ('state', models.CharField(max_length=255, null=True)),
                ('country', models.CharField(max_length=255, null=True)),
                ('zip', models.IntegerField(null=True)),
                ('catagory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.SellerCatagory')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='StoreDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255)),
                ('store_description', models.TextField(null=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='bussinessdetail',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
        migrations.AddField(
            model_name='bankdetail',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seller.Seller'),
        ),
    ]