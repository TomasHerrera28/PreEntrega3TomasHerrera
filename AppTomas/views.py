from django.shortcuts import render
from django.http import HttpResponse

def inicio(request):
    return render(request, 'AppTomas/index.html')
# Create your views here.
