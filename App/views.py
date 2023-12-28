from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Usuarios
# Create your views here.

TEMPLATES_DIR = (
    'os.path.join(BASE_DIR,"templates"),'
)

def index(request): 
    return render(request,"index.html")

def listar(request): 
    users = Usuarios.objects.all()
    datos = {'usuarios' : users}
    return render(request,"crud_usuarios/listar.html",datos)

def agregar(request):
    if request.method=='post':
        if request.post.get('nombre') and request.post.get('apellido') and request.post.get('email') and request.post.get('telefono') and request.post.get('f_nac'):
            user = Usuarios()
            user.nombre = request.post.get('nombre')
            user.apellido = request.post.get('apellido')
            user.email = request.post.get('email')
            user.telefono = request.post.get('telefono')
            user.f_nac = request.post.get('f_nac')
            user.save()
            return redirect('listar')
    else:
        return render(request,"crud_usuarios/agregar.html")
    

def actualizar(request): 
    return render(request,"crud_usuarios/actualizar.html")

def eliminar(request): 
    return render(request,"crud_usuarios/eliminar.html")