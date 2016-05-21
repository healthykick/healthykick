from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import hashers

# Import models
from .models import Seller, SellerDetail

# Create your views here.

def index(request):
	return render(request, 'seller/home.html')


def create_account(request):
	if request.method == 'POST':
		email = request.POST.get('email', False)
		password = request.POST.get('password', False)
		redirect_to = request.POST['path']

		if email and password:
			password = hashers.make_password(password, salt=None, hasher='default')
			seller = Seller.objects.create(email=email, password=password)
			context = {'seller_id': seller.id}
			return render(request, 'seller/create-account.html', context)

		else:
			messages.error(request, 'Email and Passowrd fields are required.!')
			return HttpResponseRedirect(redirect_to)


def create_seller_details(request):
	if request.method == 'POST':
		phone_number = request.POST.get('phone_number', False)
		seller_id = request.POST.get('seller_id', False)
		redirect_to = request.POST['path']

		if phone_number:
			seller_detail = SellerDetail.objects.create(mobile_number=phone_number)
			context = {'seller_id': seller_id}
			return render(request, 'seller/business-setting.html', context)
		else:
			messages.error(request, 'Phone number filed is required.!')
			return HttpResponseRedirect(redirect_to)


def create_business_details(request):
	if request.method == 'POST':
		redirect_to = request.POST['path']
		# Business Details
		business_name = request.POST.get('business_name', False)
		pan_number = request.POST.get('pan_nubmer', False)
		tin_number = request.POST.get('tin_number', False)
		tan_number = request.POST.get('tan_number', False)
		# Bank Details
		account_holder_name = request.POST.get('account_holder_name', False)
		bank_account_number = request.POST.get('bank_account_number', False)

		return True

	else:
		return False
