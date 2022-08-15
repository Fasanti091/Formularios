from django.urls import path
from productos.views import *

urlpatterns = [
    path("", index),
    path("personas/", personas)
]
