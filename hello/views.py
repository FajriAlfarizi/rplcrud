from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def salam(request):
    return HttpResponse("Welcome to Django Framework")

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'tentang.html')

def gallery(request):
    return render(request, 'gallery.html')

