# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def photos(request):
    return render(request, 'photos.html')

def videos(request):
    return render(request, 'videos.html')

def about(request):
    return render(request, 'about.html')