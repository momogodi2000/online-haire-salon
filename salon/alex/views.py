from django.shortcuts import render

def home(request):
    return render(request, 'home_page/home.html')


def services(request):
    return render(request, 'home_page/services.html')


def about(request):
    return render(request, 'home_page/about.html')

def booking(request):
    return render(request, 'home_page/booking.html')

def flyer(request):
    return render(request, 'home_page/flyer.html')
