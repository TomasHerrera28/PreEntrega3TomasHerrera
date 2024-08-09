from django.shortcuts import render
from django.http import HttpResponse
from AppTomas.forms import inciar_sesion

# Create your views here.
def inicio(request):
    return render(request, 'AppTomas/index.html')

def productos(request):
    return render(request, 'AppTomas/productos.html')

def contacto(request):
    return render(request, 'AppTomas/contacto.html')

def iniciar_sesion(request):
    
    if request.method == 'POST':
        cliente = Cliente(nombre = request.POST['nombre'], password = request.POST['password'])
    
            
            
