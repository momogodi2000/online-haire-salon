from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'), # Root URL routed to the home view
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('flyer/', views.flyer, name='flyer'),



]