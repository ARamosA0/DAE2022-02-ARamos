from django.urls import path

from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index, name='index'),
    path('producto/<int:productoid>',views.producto, name='producto'),
    path('categoria/<int:categoriaid>',views.categoria, name='categoria'),
]