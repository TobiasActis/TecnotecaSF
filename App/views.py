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
    return render(request,"crud_usuarios/listar.html", datos)

def agregar(request):
    if request.method =='POST':
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('email') and request.POST.get('telefono') and request.POST.get('f_nac'):
            user = Usuarios()
            user.nombre = request.POST.get('nombre')
            user.apellido = request.POST.get('apellido')
            user.email = request.POST.get('email')
            user.telefono = request.POST.get('telefono')
            user.f_nac = request.POST.get('f_nac')
            user.save()    
            return redirect('listar')
    else:
        return render(request,"crud_usuarios/agregar.html")
    

def actualizar(request): 
    return render(request,"crud_usuarios/actualizar.html")

def eliminar(request): 
    return render(request,"crud_usuarios/eliminar.html")