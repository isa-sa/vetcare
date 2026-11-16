from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', RedirectView.as_view(pattern_name='login', permanent=False)),
    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    path('', include('contas.urls')),
    path('clientes/', include('clientes.urls')),
    path('agendamentos/', include('agendamentos.urls')),
]