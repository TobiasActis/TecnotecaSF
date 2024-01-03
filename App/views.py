from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Usuarios
from django.utils.timezone import now
from django.db.models import Q
# Create your views here.

TEMPLATES_DIR = (
    'os.path.join(BASE_DIR,"templates"),'
)

def index(request): 
    return render(request,"index.html")

def listar(request): 
    if request.method == 'POST':
        palabra = request.POST.get('keyword') 
        lista = Usuarios.objects.all()

        if palabra is not None:
            busqueda = lista.filter(
                Q(id__icontains = palabra) |
                Q(nombre__icontains = palabra) |
                Q(apellido__icontains = palabra) |
                Q(email__icontains = palabra) |
                Q(telefono__icontains = palabra)
            )
            datos = {'usuarios' : busqueda}
            return render(request,"crud_usuarios/listar.html", datos)
        else:
            datos = {'usuarios' : lista}
            return render(request,"crud_usuarios/listar.html", datos)
    else:    
        users = Usuarios.objects.order_by('-id')[:10]
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
    

def actualizar(request, idUsuario):
    try:
        if request.method == 'POST':
            if request.POST.get('id') and request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('email') and request.POST.get('telefono') and request.POST.get('f_nac'):
                id_old = request.POST.get('id')
                user_old = Usuarios()
                user_old = Usuarios.objects.get(id = id_old)
                
                user = Usuarios()
                user.id = request.POST.get('id')
                user.nombre = request.POST.get('nombre')
                user.apellido = request.POST.get('apellido')
                user.email = request.POST.get('email')
                user.telefono = request.POST.get('telefono')
                user.f_nac = request.POST.get('f_nac')
                user.f_registro = user_old.f_registro
                user.save()    
                return redirect('listar')
        else:
            users = Usuarios.objects.all()
            user = Usuarios.objects.get( id =  idUsuario)
            datos = {'usuarios' : users , 'usuario' : user} 
            return render(request,"crud_usuarios/actualizar.html", datos)
   
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = {'usuarios' : users , 'usuario' : user} 
        return render(request,"crud_usuarios/actualizar.html", datos)

def eliminar(request, idUsuario): 
    try:
        if request.method == 'POST':
            if request.POST.get('id'):
                id_eliminada = request.POST.get('id')
                tupla = Usuarios.objects.get(id=id_eliminada)
                tupla.delete()
                return redirect('listar')
        else:    
            users = Usuarios.objects.all()
            user = Usuarios.objects.get(id=idUsuario)
            datos = {'usuarios': users, 'usuario': user} 
            return render(request, "crud_usuarios/eliminar.html", datos)
    
    except Usuarios.DoesNotExist:
        users = Usuarios.objects.all()
        user = None
        datos = {'usuarios': users, 'usuario': user} 
        return render(request, "crud_usuarios/eliminar.html", datos)
