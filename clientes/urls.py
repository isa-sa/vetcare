from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('tutores/novo/', views.cadastrar_tutor, name='cadastrar_tutor'),
    path('pets/novo/', views.cadastrar_pet, name='cadastrar_pet'),
]