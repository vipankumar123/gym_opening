from django.urls import path
from gym.views import*

urlpatterns=[
	path('admin1/',home),
	path('admin2/',about),
	path('admin3/',contact),
	path('admin4/',login, name='loginpage'),
	path('admin5/',register),
	path('admin6/',add_enquiry),
	path('admin7/',view_enquiry),
	path('admin8/<int:id>/',delete_enquiry),
	path('admin9/',add_equipment),
	path('admin10/',view_equipment),
	path('admin11/<int:id>/',delete_equipment),
	path('admin12/',add_plan),
	path('admin13/',view_plan),
	path('admin14/<int:id>/',delete_plan),
	path('admin15/',add_member),
	path('admin16/',view_member),
	path('admin17/<int:id>/',delete_member),

]