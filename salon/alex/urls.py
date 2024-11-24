from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django_distill import distill_path


def get_index():
    return None



urlpatterns = [
    path('', views.home, name='home'), # Root URL routed to the home view
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('booking/', views.booking, name='booking'),
    path('flyer/', views.flyer, name='flyer'),

    distill_path('', views.home, name='home', distill_func=get_index),



]