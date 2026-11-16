from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_agenda, name='listar_agenda'),
    path('novo/', views.novo_agendamento, name='novo_agendamento'),
    path('<int:consulta_id>/status/', views.mudar_status_consulta, name='mudar_status_consulta'),
]