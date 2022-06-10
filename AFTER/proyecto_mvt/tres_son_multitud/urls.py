from django.urls import path
from . import views




urlpatterns = [
    
   path("", views.inicio),
   path("parientes" , views.Parientes), 
   path("registro/", views.registro_parientes),
   path("alta_caracteristicas" , views.alta_caracteristicas),
   path("alta_educacion" , views.alta_educacion),
   path("alta_parientes , views.alta_parientes")
    
    
    
]
