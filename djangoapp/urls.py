"""djangoapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hello.views import *
from myapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    #tambahan app hello
    path('salam/', salam, name='salam'),
    path('beranda/', home, name='home'),
    path('about/', about, name='aboutus'),
    path('gallery/', gallery, name='gallery'),
    #tambahan app myapp
    path('', beranda, name='beranda'),
    path('home/', beranda, name='beranda'),
    path('aboutus/', aboutus, name='tentang_kami'),
    path('login/', login, name='login'),
    path('gallery1/', gallery1, name='gallery1'),
    path('Anggota/', getAnggota, name='Anggota' ),
    path('Buku/', getBuku, name='Buku' ),
    path('Pinjam/', getPinjam, name='Pinjam' ),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout')
]
