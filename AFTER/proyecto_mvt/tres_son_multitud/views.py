import http
from django.shortcuts import render
from tres_son_multitud.models import parientes
from django.http import HttpResponse
import datetime



def inicio(request):
    return render(request , "index.html")


def Parientes(request):
    integrantes = parientes.objects.all()
    datos = { "datos" : integrantes }
    
    return render( request , "lista_parientes.html" , datos)

def registro_parientes(request):
    parientes1 = parientes(nombre="Manolo" , apellidos="Gutierrez" , edad=40 , cumpleaños="1982-04-20", locacion="Caracas")
    parientes1.save()
    parientes2 = parientes(nombre="Perucho" , apellidos="Conde" , edad=39 , cumpleaños="1983-06-09", locacion="NY")
    parientes2.save()
    parientes3 = parientes(nombre="Debora" , apellidos="Meltroso" , edad=37 , cumpleaños="1984-08-25", locacion="Pernambuco")
    parientes3.save()
    
    return HttpResponse("la app esta en un estado optimo")
    