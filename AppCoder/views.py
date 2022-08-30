from django.shortcuts import render
from .models import Curso, Estudiante
from django.http import HttpResponse
# Create your views here.

def curso(request):

    
    nombre = request.POST.get("nombre")
    comision = request.POST.get("comision")
    curso = Curso(nombre=nombre, comision=comision)
    curso.save()
    curso=Curso(nombre="curso creado en el ejemplo", comision=0)
    print("CREANDO CURSO")
    curso.save()
    
    texto=f"curso creado"
    return HttpResponse(texto)

def inicio(request):
    return render (request, "AppCoder/inicio.html")

def cursos(request):
    return render (request, "AppCoder/cursos.html")


def estudiantes(request):
    return render (request, "AppCoder/estudiantes.html")

def profesores(request):
    return render (request, "AppCoder/profesores.html")

def entregables(request):
    return render (request, "AppCoder/entregables.html")








