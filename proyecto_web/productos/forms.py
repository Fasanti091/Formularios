from  django.forms import Form, CharField

# Formulario de busqueda

class Busqueda(Form):
    nombre_producto = CharField(max_length=150)
    