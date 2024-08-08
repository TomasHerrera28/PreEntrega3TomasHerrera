from django.urls import path
from AppTomas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('productos/', views.productos, name="Productos"),
    path('contacto/', views.contacto, name="Contacto")
]