from __future__ import unicode_literals

from django.db import models
import datetime

# Create your models here.

class Seller(models.Model):
	email = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	name = models.CharField(max_length=255, blank=True)
	active = models.NullBooleanField()
	created_at = models.DateTimeField('Created Date', default=datetime.datetime.now())
	updated_at = models.DateTimeField('Updated Date', default=datetime.datetime.now())

	def __str__(self):              # __unicode__ on Python 3
		return str(self.email)


class SellerDetail(models.Model):
	seller = models.ForeignKey(Seller)
	mobile_number = models.IntegerField(null=True)
	address = models.TextField(null=True)
	city = models.CharField(max_length=255, null=True)
	state = models.CharField(max_length=255, null=True)
	country = models.CharField(max_length=255, null=True)
	zip = models.IntegerField(null=True)

	def __str__(self):
		return str(self.seller)


class BussinessDetail(models.Model):
	seller = models.ForeignKey(Seller)
	bussiness_name = models.CharField(max_length=255)
	pan_number = models.IntegerField(null=False)
	tin_number = models.IntegerField(null=False)
	tan_number = models.IntegerField(null=False)

	def __str__(self):
		return str(self.bussiness_name)


class BankDetail(models.Model):
	seller = models.ForeignKey(Seller)
	account_holder_name = models.CharField(max_length=255)
	bank_account_number = models.IntegerField(null=False)
	ifsc_code = models.CharField(max_length=20)
	bank_name = models.CharField(max_length=255)
	bank_branch = models.CharField(max_length=255)
	bank_state = models.CharField(max_length=255)
	bank_city = models.CharField(max_length=255)

	def __str__(self):
		return str(self.account_holder_name)


class StoreDetail(models.Model):
	seller = models.ForeignKey(Seller)
	store_name = models.CharField(max_length=255)
	store_description = models.TextField(null=True)

	def __str__(self):
		return str(self.store_name)


class Catagory(models.Model):
	catagory_name = models.CharField(max_length=255)
	catagory_alias = models.CharField(max_length=255)


class SellerCatagory(models.Model):
	seller = models.ForeignKey(Seller)
	catagory = models.ForeignKey(Catagory)


class SellerSetting(models.Model):
	seller = models.ForeignKey(Seller)
	pickup_address = models.TextField(null=True)
	city = models.CharField(max_length=255, null=True)
	state = models.CharField(max_length=255, null=True)
	country = models.CharField(max_length=255, null=True)
	zip = models.IntegerField(null=True)
	catagory = models.ForeignKey(SellerCatagory)

	def __str__(self):
		return str(self.seller)