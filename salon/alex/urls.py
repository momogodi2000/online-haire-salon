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
    distill_path('about/', views.about, name='about', distill_func=get_index),
    distill_path('services/', views.services, name='services', distill_func=get_index),
    distill_path('booking/', views.booking, name='booking', distill_func=get_index),
    distill_path('flyer/', views.flyer, name='flyer', distill_func=get_index),




]