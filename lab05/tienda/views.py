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
    lista_categoria = Categoria.objects.all()
    context={
        'producto':producto,
        'lista_categoria':lista_categoria
    }
    return render(request,"producto.html", context)

def categoria(request,categoriaid):
    lista_categoria = Categoria.objects.all()
    categoria = Categoria.objects.get(id=categoriaid)
    lista_productos = Producto.objects.filter(categoria = categoriaid)
    context = {
        'categoria':categoria,
        'lista_categoria':lista_categoria,
        'lista_productos':lista_productos
    }
    return render(request, "categoria.html", context)