"""
URL configuration for web_amr project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from web import views
from django.conf import settings             
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.beranda, name='beranda'), # <--- Path kosong '' berarti halaman utama (home)
    path('ajax/mahasiswa/', views.mahasiswa_json, name='mahasiswa_datatable'),
    path('api/klasemen/', views.klasemen_datatable, name='klasemen_datatable'),
    path('gabung-komunitas/', views.gabung_komunitas, name='gabung_komunitas'),
    path('daftar-tim/', views.daftar_tim, name='daftar_tim'),
    path('cek-jadwal/', views.cek_jadwal, name='cek_jadwal'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)