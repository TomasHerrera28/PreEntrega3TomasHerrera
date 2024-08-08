from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def inicio(request):
    return render(request, 'AppTomas/index.html')

def productos(request):
    return render(request, 'AppTomas/productos.html')

def contacto(request):
    return render(request, 'AppTomas/contacto.html')
