from django.urls import path

from . import views

app_name = 'cursos'

urlpatterns  = [
    path('', views.index, name='index'),
    path('semestre/<int:id>/', views.filtSemestre, name='cursos')
]