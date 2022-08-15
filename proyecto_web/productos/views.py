from http.client import HTTPResponse
from django.shortcuts import render
from productos.models import *
from productos.forms import Busqueda

# Create your views here.
def index(request):
    # Agregar la lista
    listado_productos = Producto.objects.all()

    # Buscador <----
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_productos = Producto.objects.filter(nombre__icontains = data["buscar"])
        
        return render(request, "productos/index.html", {"productos": listado_productos, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request, "productos/index.html", {"productos" : listado_productos, "formulario" : formulario})

def personas(request):
    # Agregar la lista
    listado_personas = Personas.objects.all()

    # Buscador <----
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_personas = Personas.objects.filter(nombre__icontains = data["buscar"])
        
        return render(request, "productos/personas.html", {"personas": listado_personas, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request, "productos/personas.html", {"personas": listado_personas, "formulario" : formulario})

def ciudades(request):
    # Agregar la lista
    listado_ciudades = Ciudades.objects.all()

    # Buscador <----
    if request.GET.get("buscar"):
        
        formulario = Busqueda(request.GET)

        if formulario.is_valid():
            data = formulario.cleaned_data
            listado_ciudades = Ciudades.objects.filter(nombre__icontains = data["buscar"])
        
        return render(request, "productos/ciudades.html", {"ciudades": listado_ciudades, "formulario" : formulario})

    else:
        formulario = Busqueda()
        return render(request, "productos/ciudades.html", {"ciudades": listado_ciudades, "formulario" : formulario})


def formulario_productos(request):
    if request.method == "POST":

        nombre = request.POST["nombre"]
        marca = request.POST["marca"]
        precio = request.POST["precio"]
        fecha_vencimiento = request.POST["fecha_vencimiento"]
        stock = request.POST["stock"]

        productos = Producto(nombre=nombre, marca=marca, precio=precio, fecha_vencimiento=fecha_vencimiento, stock=stock)
        productos.save()
        
        return render(request, "productos/index.html")
    else:
        return render(request, "productos/formulario_productos.html")

def formulario_personas(request):
    if request.method == "POST":

        nombre = request.POST["nombre"]
        apellido = request.POST["apellido"]
        edad = request.POST["edad"]

        productos = Personas(nombre=nombre, apellido=apellido, edad=edad)
        productos.save()
        
        
        return render(request, "productos/personas.html")
    else:
        return render(request, "productos/formulario_personas.html")

def formulario_ciudades(request):
    if request.method == "POST":

        nombre = request.POST["nombre"]
        pais = request.POST["pais"]
        municipio = request.POST["municipio"]

        productos = Ciudades(nombre=nombre, pais=pais, municipio=municipio)
        productos.save()
        
        
        return render(request, "productos/ciudades.html")
    else:
        return render(request, "productos/formulario_ciudades.html")
    
    
    