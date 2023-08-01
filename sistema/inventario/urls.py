from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name="inicio"),
    path('productos/', views.productos, name="productos"),
    path('categorias/', views.categorias, name="categorias"),
    path('usuarios/', views.usuarios, name="usuarios"),
    path('roles/', views.roles, name="roles"),
    path('list_users/', views.list_users, name='list_users')
]