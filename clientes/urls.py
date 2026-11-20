from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_clientes, name='listar_clientes'),
    path('tutores/novo/', views.cadastrar_tutor, name='cadastrar_tutor'),
    path('tutores/<int:tutor_id>/editar/', views.editar_tutor, name='editar_tutor'),
    path('tutores/<int:tutor_id>/excluir/', views.excluir_tutor, name='excluir_tutor'),
    path('pets/novo/', views.cadastrar_pet, name='cadastrar_pet'),
    path('pets/<int:pet_id>/editar/', views.editar_pet, name='editar_pet'),
    path('pets/<int:pet_id>/excluir/', views.excluir_pet, name='excluir_pet'),
]