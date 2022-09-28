from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from .models import Producto,Categoria,Cliente

def index(request):
    product_list = Producto.objects.all()
    lista_categoria = Categoria.objects.all()
    context = {
        'product_list':product_list,
        'lista_categoria':lista_categoria
    }
    return render(request,"index.html", context)

def producto(request, productoid):
    producto = Producto.objects.get(id=productoid)
    context={
        'producto':producto
    }
    return render(request,"producto.html", context)

def categoria(request,categoriaid):
    categoria = Categoria.objects.get(id=categoriaid)