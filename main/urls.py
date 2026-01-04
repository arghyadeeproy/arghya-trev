from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listing',views.listing, name='listing'),
    path('login',views.login, name='login'),
    path('hotel',views.hotel, name='hotel'),
    path('payment',views.payment, name='payment')
]
