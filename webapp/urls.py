from django.contrib import admin
from django.urls import path, include 
from contas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('contas/', include('django.contrib.auth.urls')), 
    path('contas/', include('contas.urls')),

    path('', views.index, name='index')
]