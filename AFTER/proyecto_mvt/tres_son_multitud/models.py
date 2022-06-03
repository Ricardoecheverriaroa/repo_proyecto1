from django.db import models

# Create your models here.


class parientes(models.Model):
    
    nombre = models.CharField(max_length=40)
    apellidos = models.CharField(max_length=40)
    edad = models.IntegerField()
    cumpleaños = models.DateField()
    locacion = models.CharField(max_length=40)
    
class educacion(models.Model):
    
    secundario = models.CharField(max_length=40)
    tecnico = models.CharField(max_length=40)
    licenciatura = models.CharField(max_length=40)
    postgrado = models.CharField(max_length=40)
    maestria = models.CharField(max_length=40)
    doctorado = models.CharField(max_length=40)
    
class caracteristicas(models.Model):
    
    comidas = models.CharField(max_length=40)
    colores = models.CharField(max_length=40)
    signo = models.CharField(max_length=40)
    estatura = models.IntegerField()
    peso = models.IntegerField()
    
    
    