from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import hashers
from django.contrib import messages

# Import models
from .models import Seller, SellerDetail, BussinessDetail, BankDetail, StoreDetail
from .authentication import login_required

# Create your views here.

def index(request):
	return render(request, 'seller/home.html')


def login(request):
    redirect_to = '/seller/seller_dashboard/'
    
    try:
        seller = Seller.objects.get(email=request.POST.get('email', ''))
    except Seller.DoesNotExist:
        seller = None
    
    if not seller:
        messages.error(request, 'User not found!')
        return HttpResponseRedirect("/seller/")
    else:
        if hashers.check_password(request.POST['password'], seller.password, setter=None, preferred='default'):
            request.session['email'] = seller.email
            return HttpResponseRedirect(redirect_to)
        else:
            messages.warning(request, "Password didn't match!")
            return HttpResponseRedirect("/seller/")


@login_required(login_url='/seller')
def logout(request):
	try:
		del request.session['email']
	except KeyError:
		pass
	return HttpResponseRedirect('/seller/')


def create_account(request):
	if request.method == 'POST':
		email = request.POST.get('email', False)
		password = request.POST.get('password', False)
		

		try:
			seller = Seller.objects.get(email=email)
		except Seller.DoesNotExist:
			seller = None

		if seller is None:
			if email and password:
				password = hashers.make_password(password, salt=None, hasher='default')
				seller = Seller.objects.create(email=email, password=password)
				request.session['seller_id'] = seller.id
				redirect_to = 'create_seller_details'

			else:
				messages.error(request, 'Email and Passowrd fields are required.!')
				redirect_to = request.POST['path']
		else:
			messages.error(request, 'Already registered.')
			redirect_to = request.POST['path']
		
		return HttpResponseRedirect(redirect_to)


def create_seller_details(request):
	if request.method == 'GET':

		context = {'seller_id': request.session.get('seller_id', False)}

		return render(request, 'seller/create-account.html', context)

	if request.method == 'POST':
		phone_number = request.POST.get('phone_number', False)
		seller_id = request.POST.get('seller_id', False)
		redirect_to = request.POST['path']

		try:
			seller = Seller.objects.get(id=seller_id)
		except Seller.DoesNotExist:
			seller = None

		if phone_number and seller is not None:
			seller_detail = SellerDetail.objects.create(seller=seller, mobile_number=int(phone_number))
			return HttpResponseRedirect('create_business_details')
		else:
			messages.error(request, 'Phone number filed is required.!')
			return HttpResponseRedirect('create_seller_details')


def create_business_details(request):
	if request.method == 'GET':
		
		context = {'seller_id': request.session.get('seller_id', False)}
		
		return render(request, 'seller/business-setting.html', context)

	if request.method == 'POST':
		redirect_to = request.POST['path']
		
		#Seller
		seller_id = request.POST.get('seller_id', False)
		try:
			seller = Seller.objects.get(id=seller_id)
		except Seller.DoesNotExist:
			seller = None
		
		# Business Details
		business_name = request.POST.get('business_name', False)
		pan_number = request.POST.get('pan_number', False)
		tin_number = request.POST.get('tin_number', False)
		tan_number = request.POST.get('tan_number', False)
		
		# Bank Details
		account_holder_name = request.POST.get('account_holder_name', False)
		bank_account_number = request.POST.get('bank_account_number', False)
		ifsc_code = request.POST.get('ifsc_code', False)
		bank_name = request.POST.get('bank_name', False)
		bank_branch = request.POST.get('bank_branch', False)
		bank_state = request.POST.get('bank_state', False)
		bank_city = request.POST.get('bank_city', False)

		#Store Details
		store_name = request.POST.get('store_name', False)
		store_description = request.POST.get('store_description', False)

		if seller is not None and business_name and pan_number and tin_number and tan_number and account_holder_name and bank_account_number and ifsc_code and bank_name and bank_branch and bank_state and bank_city and store_name and store_description:
			business_details = BussinessDetail.objects.create(seller=seller, bussiness_name=business_name, pan_number=pan_number, tin_number=tin_number, tan_number=tan_number)
			bank_details = BankDetail.objects.create(seller=seller, account_holder_name=account_holder_name, bank_account_number=bank_account_number, ifsc_code=ifsc_code, bank_name=bank_name, bank_branch=bank_branch, bank_state=bank_state, bank_city=bank_city)
			store_detail = StoreDetail.objects.create(seller=seller, store_name=store_name, store_description=store_description)

			return HttpResponseRedirect('/seller/seller_dashboard/')
		else:
			messages.error(request, 'All fileds are mendatory.!')
			return HttpResponseRedirect('create_business_details')



		return True

	else:
		return False


@login_required(login_url='/seller')
def seller_dashboard(request):
	if request.method == 'GET':
		return render(request, 'seller/penal/dashboard.html')