from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
# Create your views here.

def curso(request):
    curso=Curso(nombre="AWS", comision=3)
    curso2=Curso(nombre="Lengua", comision=1)
    curso3=Curso(nombre="Matematica", comision=2)
    curso.save()
    curso2.save()
    curso3.save()
    texto=f"cursos creados"
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




