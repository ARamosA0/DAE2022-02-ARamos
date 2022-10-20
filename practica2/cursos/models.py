from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Semestre(models.Model):
    nombre = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre


class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=500)
    semestre = models.ForeignKey(Semestre, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre