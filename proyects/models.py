from django.db import models

# Create your models here.

class Proyect(models.Model):
    proyectos = models.CharField(max_length=200)
    rut =  models.CharField(max_length=200)
    nombre_integrante = models.CharField(max_length=200)
    fec_creacion = models.DateTimeField(auto_now_add=True)