from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('',views.index, name= "index"),
    path('listar',views.listar, name= "listar"),
    path('agregar',views.agregar, name= "agregar"),
    path('actualizar/<int:idUsuario>',views.actualizar, name= "actualizar"),
    path('eliminar/<int:idUsuario>',views.eliminar, name= "eliminar"),
    path('listarEventos',views.listarEventos, name= "listarEventos"),
    path('agregarEventos',views.agregarEventos, name= "agregarEventos"),
    path('actualizarEventos/<int:idEvento>',views.actualizarEventos, name= "actualizarEventos"),
    path('eliminarEventos/<int:idEvento>',views.eliminarEventos, name= "eliminarEventos"),

]