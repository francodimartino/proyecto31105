
from django.urls import path
from AppCoder.views import *

urlpatterns = [
    
    path("curso/", curso),
    path("", inicio, name="inicio"),
    
    path("estudiantes/", estudiantes, name="estudiantes"),
    path("profesores/", profesores, name="profesores"),
    path("entregables/", entregables, name="entregables"),
    path("cursos/", cursos, name="cursos"),
    path("profeFormulario/", profeFormulario, name="profeFormulario"),
    path("busquedaComision/", busquedaComision, name="busquedaComision"),
    path("buscar/", buscar, name="buscar"),
    
]
