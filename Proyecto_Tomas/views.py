from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola mundo")

def probando_template(request):
    
    nombre = "Tomas"
    apellido = "Herrera"
    diccionario = {"nombre": nombre, "apellido": apellido}
    
    mi_html = open('./Proyecto_Tomas/plantillas/index.html')
    
    plantilla = Template(mi_html.read())
    
    mi_html.close()
    
    mi_contexto = Context(diccionario)
    
    documento = plantilla.render(mi_contexto)
    
    return HttpResponse(documento)