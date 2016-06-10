from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'login', views.login, name='login'),
	url(r'logout', views.logout, name='logout'),
	url(r'create_account', views.create_account, name='create_account'),
	url(r'create_seller_details', views.create_seller_details, name='create_seller_details'),
	url(r'create_business_details', views.create_business_details, name='create_business_details'),
	url(r'seller_dashboard', views.seller_dashboard, name='seller_dashboard'),
]