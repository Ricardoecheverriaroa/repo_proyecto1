from django.urls import path
from . import views




urlpatterns = [
    
   path("", views.inicio),
   path("parientes" , views.Parientes), 
   path("registro/", views.registro_parientes)
    
    
    
]
