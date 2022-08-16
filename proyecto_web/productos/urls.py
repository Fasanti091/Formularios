from django.urls import path
from productos.views import *

urlpatterns = [
    path("", index, name='productos'),
    path("personas/", personas, name='personas'),
    path("ciudades/", ciudades, name='ciudades'),
    path('formulario_productos/', formulario_productos, name='formulario_productos'),
    path('formulario_personas/', formulario_personas, name='formulario_personas'),
    path('formulario_ciudades/', formulario_ciudades, name='formulario_ciudades')

]
