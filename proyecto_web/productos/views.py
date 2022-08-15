from http.client import HTTPResponse
from django.shortcuts import render
from productos.models import *
from productos.forms import Busqueda

# Create your views here.
def index(request):

    listado_productos = Producto.objects.all()

    if request.GET.get("nombre_producto"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Producto.objects.filter(nombre__icontains = data["nombre_producto"])
        
        return render(request, "productos/index.html", {"productos": listado_productos, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request, "productos/index.html", {"productos" : listado_productos, "formulario" : formulario})

def personas(request):
    listado_personas = Personas.objects.all()

    return render(request, "productos/personas.html", {"personas" : listado_personas})



