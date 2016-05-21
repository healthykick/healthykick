from django.conf.urls import url

from . import views


urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'create_account', views.create_account, name='create_account'),
	url(r'create_seller_details', views.create_seller_details, name='create_seller_details'),
	url(r'create_business_details', views.create_business_details, name='create_business_details')
]