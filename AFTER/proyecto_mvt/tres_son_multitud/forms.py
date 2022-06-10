from django import forms


class parientes_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=40)
    apellidos = forms.CharField(max_length=40)
    edad = forms.IntegerField()
    cumpleaños = forms.DateField()
    locacion = forms.CharField(max_length=40)
    
class educacion_formulario(forms.Form):
    
    secundario = forms.CharField(max_length=40)
    tecnico = forms.CharField(max_length=40)
    licenciatura = forms.CharField(max_length=40)
    postgrado = forms.CharField(max_length=40)
    maestria = forms.CharField(max_length=40)
    doctorado = forms.CharField(max_length=40)
    
class carracteristicas_formulario(forms.Form):
    
    comidas = forms.CharField(max_length=40)
    colores = forms.CharField(max_length=40)
    signo = forms.CharField(max_length=40)
    estatura = forms.IntegerField()
    peso = forms.IntegerField()
    