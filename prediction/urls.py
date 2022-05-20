from django.urls import path
from . import views

urlpatterns= [
	path('',views.index, name='index'),
	path('companies/',views.companies, name='companies'),
	path('philips/',views.philips, name='philips'),
	path('dell/',views.dell, name='dell'),
	path('apply/',views.apply, name='apply'),
	path('login/',views.login, name='login'),
	path('marks/',views.marks, name='marks'),
]