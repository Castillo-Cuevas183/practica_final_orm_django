from django.urls import path
from . import views

urlpatterns = [
    path('crear/', views.crear_laboratorio, name='crear_laboratorio'),
    path('', views.listar_laboratorios, name='listar_laboratorios'),
    path('editar/<int:id>/', views.editar_laboratorio, name='editar_laboratorio'),
    path('eliminar/<int:id>/', views.eliminar_laboratorio, name='eliminar_laboratorio'),
    
    
]
