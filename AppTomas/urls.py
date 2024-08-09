from django.urls import path
from AppTomas import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('productos/', views.productos, name="Productos"),
    path('contacto/', views.contacto, name="Contacto"),
    path('form-con-api/', views.form_con_api, name="Form-Con-Api")
]