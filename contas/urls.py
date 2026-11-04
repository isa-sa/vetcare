from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.signup, name='signup'),

    path('painel/', views.painel, name='painel'),
]