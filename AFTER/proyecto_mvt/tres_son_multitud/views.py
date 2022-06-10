import http
from django.shortcuts import render
from proyecto_mvt.tres_son_multitud.forms import parientes_formulario, caracteristicas_formulario , educacion_formulario
from proyecto_mvt.tres_son_multitud.models import caracteristicas, educacion, Caracteristicas,  Educacion
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

def alta_caracteristicas(request):
    
    if request.method == "POST":
        
        mi_formulario = caracteristicas_formulario( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
            caracteristicas = Caracteristicas( comidas=datos[ 'comidas' ] , colores=datos[ 'colores' ] , signo=datos[ 'signo' ] , estatura=datos[ 'estatura' ] , peso=datos[ 'peso' ] )
            caracteristicas.save()
            
            return HttpResponse("SE CREO LA CARACTERISTICA")
            
        return render(request, "alta_caracteristicas.html")

def alta_educacion(request):

    if request.method == "POST":
        
        mi_formulario = educacion_formulario( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
            educacion = Educacion( secundario=datos[ 'secundario' ] ,  tecnico=datos[ ' tecnico' ] , licenciatura=datos[ 'licenciatura' ] , postgrado=datos[ 'postgrado' ] ,  maestria=datos[ ' maestria' ] ,  doctorado=datos[ ' doctorado' ] )
            educacion.save()
            
            return HttpResponse("SE INGRESO EL NIVEL EDUCATIVO")
        
        return render(request, "alta_educacion.html")
    
def alta_parientes(request):
    
    if request.method == "POST":
        
        mi_formulario = parientes_formulario( request.POST )
        
        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data
            
            parientes = Parientes( nombres=datos[ 'nombres' ] , apellidos=datos[ 'apellidos' ] , edad=datos[ 'edad' ] , cumpleaños=datos[ 'cumpleaños' ] , locacion=datos[ 'locacion' ] )
            parientes.save()
            
            return HttpResponse("SE INGRESO EL FAMILIAR")
            
        return render(request, "alta_parientes.html")
    

    
    

