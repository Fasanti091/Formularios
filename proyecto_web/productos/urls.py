from django.urls import path
from productos.views import index

urlpatterns = [
    path("", index)
]
