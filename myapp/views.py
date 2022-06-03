from django.shortcuts import render
from .models import *

# Create your views here.
def beranda(request):
    return render(request, 'beranda.html')

def aboutus(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

def getAnggota(request):
    Anggota_list = TableAnggota.objects.all()
    template = 'anggota.html'
    context = {
        'Anggota_list' : Anggota_list
    } 
    return render(request, template, context)

def getBuku(request):
    Buku_list = TableBuku.objects.all()
    template = 'buku.html'
    context = {
        'Buku_list' : Buku_list
    } 
    return render(request, template, context)

def getPinjam(request):
    Pinjam_list = TablePinjam.objects.all()
    template = 'pinjam.html'
    context = {
        'Pinjam_list' : Pinjam_list
    } 
    return render(request, template, context)

def login(request):
    return render(request, 'login.html')


def logout(request):
    return render(request, 'logout.html')

def gallery1(request):
    return render(request, 'gallery1.html')