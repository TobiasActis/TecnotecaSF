from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name= "index"),
    path('listar',views.listar, name= "listar"),
    path('agregar',views.agregar, name= "agregar"),
    path('actualizar',views.actualizar, name= "actualizar"),
    path('eliminar',views.eliminar, name= "eliminar"),
   
]