from django.contrib import admin
from AppTomas.models import Producto, Carrito, Cliente

# Register your models here.
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Carrito)