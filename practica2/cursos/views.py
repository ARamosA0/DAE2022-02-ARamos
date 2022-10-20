from multiprocessing import context
from django.shortcuts import render

# Create your views here.

from .models import Semestre, Curso

def index(request):
    lista_cursos = Curso.objects.all()
    lista_semestre = Semestre.objects.all()
    context = {
        'lista_cursos':lista_cursos,
        'lista_semestre':lista_semestre
    }

    return render(request, "index.html", context)


def filtSemestre(request, id):
    lista_cursos_fil = Curso.objects.filter(semestre = id)
    print(lista_cursos_fil)
    context = {
        'lista_cursos_fil':lista_cursos_fil
    }

    return render(request, "cursos.html", context)