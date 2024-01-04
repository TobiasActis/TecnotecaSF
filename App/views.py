from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .models import Usuarios
from .models import Eventos
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



def listarEventos(request): 
    if request.method == 'POST':
        palabra = request.POST.get('keyword') 
        lista = Eventos.objects.all()

        if palabra is not None:
            busqueda = lista.filter(
                Q(id__icontains = palabra) |
                Q(descripcion__icontains = palabra) 
            )
            datos = {'eventos' : busqueda}
            return render(request,"crud_eventos/listarEventos.html", datos)
        else:
            datos = {'eventos' : lista}
            return render(request,"crud_eventos/listarEventos.html", datos)
    else:    
        events = Eventos.objects.order_by('-id')[:10]
        datos = {'eventos' : events}
        return render(request,"crud_eventos/listarEventos.html", datos)
    
def agregarEventos(request):
    if request.method =='POST':
        if request.POST.get('descripcion') and request.POST.get('fecha') and request.POST.get('hora'):
            event = Eventos()
            event.descripcion = request.POST.get('descripcion')
            event.fecha = request.POST.get('fecha')
            event.hora = request.POST.get('hora')
            event.save()    
            return redirect('listar')
    else:
        return render(request,"crud_eventos/agregarEventos.html")
    

def actualizarEventos(request, idEvento):
    try:
        if request.method == 'POST':
            if request.POST.get('id') and request.POST.get('descripcion') and request.POST.get('fecha') and request.POST.get('hora'):
                id_old = request.POST.get('id')
                event_old = Eventos()
                event_old = Eventos.objects.get(id = id_old)
                
                event = Usuarios()
                event.id = request.POST.get('id')
                event.descripcion = request.POST.get('descripcion')
                event.fecha = request.POST.get('fecha')
                event.hora = request.POST.get('hora')
                event.f_registro = event_old.f_registro
                event.save()    
                return redirect('listarEventos')
        else:
            events = Eventos.objects.all()
            event = Eventos.objects.get( id =  idEvento)
            datos = {'eventos' : events , 'evento' : event} 
            return render(request,"crud_eventos/actualizarEventos.html", datos)
   
    except Eventos.DoesNotExist:
        events = Eventos.objects.all()
        event = None
        datos = {'eventos' : events , 'evento' : event} 
        return render(request,"crud_eventos/actualizarEventos.html", datos)
    

def eliminarEventos(request, idEvento): 
    try:
        if request.method == 'POST':
            if request.POST.get('id'):
                id_eliminada = request.POST.get('id')
                tupla = Eventos.objects.get(id=id_eliminada)
                tupla.delete()
                return redirect('listarEventos')
        else:    
            events = Eventos.objects.all()
            event = Eventos.objects.get(id=idEvento)
            datos = {'eventos': events, 'evento': event} 
            return render(request, "crud_eventos/eliminarEventos.html", datos)
    
    except Eventos.DoesNotExist:
        events = Eventos.objects.all()
        event = None
        datos = {'eventos': events, 'event': event} 
        return render(request, "crud_eventos/eliminarEventos.html", datos)
