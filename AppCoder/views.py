from django.shortcuts import render
from .models import Curso, Estudiante, Profesor
from django.http import HttpResponse

from AppCoder.forms import CursoForm, ProfeForm, UserRegisterForm
from django.urls import reverse_lazy


from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

@login_required
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

""" def cursoFormulario(request):
    if request.method=="POST":
        nombre=request.POST["nombre"]
        comision=request.POST["comision"]
        curso=Curso(nombre=nombre, comision=comision)
        curso.save()
        return render (request, "AppCoder/inicio.html")
    
    return render (request, "AppCoder/cursoFormulario.html") """

def cursos(request):
    if request.method=="POST":
        form=CursoForm(request.POST)
        print("-------------------------------")
        print(form)
        print("-------------------------------")
        if form.is_valid():
            informacion=form.cleaned_data
            print(informacion)
            nombre=informacion["nombre"]
            comision=informacion["comision"]
            curso=Curso(nombre=nombre, comision=comision)
            curso.save()
            return render (request, "AppCoder/inicio.html")


    else:
        formulario=CursoForm()
        return render (request, "AppCoder/cursos.html", {"formulario":formulario})


def profeFormulario(request):

    if request.method=="POST":
        form= ProfeForm(request.POST)
        if form.is_valid():
            info= form.cleaned_data
            nombre= info["nombre"]
            apellido= info["apellido"]
            email= info["email"]
            profesion= info["profesion"]
            profe= Profesor(nombre=nombre, apellido=apellido, email=email, profesion=profesion)
            profe.save()
            profesores=Profesor.objects.all()
    
            return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})
    else:
        form= ProfeForm()
    return render(request, "Appcoder/profeForm.html", {"formulario":form})



##........................

def busquedaComision(request):
    return render(request, "Appcoder/busquedaComision.html")

def buscar(request):
    if request.GET["comision"]:

        comision=request.GET["comision"]
        #traeme de la base, TODOS los cursos que tengan esa comision
        cursos=Curso.objects.filter(comision=comision)
        return render(request, "Appcoder/resultadosBusqueda.html", {"cursos":cursos})
    else:
        return render(request, "Appcoder/busquedaComision.html", {"mensaje":"CHE! Ingresa una comision"})
    
    return HttpResponse(respuesta)

@login_required
def leerProfesores(request):
    profesores=Profesor.objects.all()
    print(list(profesores))
    return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})

def eliminarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    profesor.delete()
    profesores=Profesor.objects.all()
    return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})


def editarProfesor(request, id):
    profesor=Profesor.objects.get(id=id)
    if request.method=="POST":
        form=ProfeForm(request.POST)
        if form.is_valid():
            #cambio los datos
            info=form.cleaned_data
            profesor.nombre=info["nombre"]
            profesor.apellido=info["apellido"]
            profesor.email=info["email"]
            profesor.profesion=info["profesion"]
            profesor.save()
            profesores=Profesor.objects.all()
            return render(request, "Appcoder/leerProfesores.html", {"profesores":profesores})
    else:
        form= ProfeForm(initial={"nombre":profesor.nombre, "apellido":profesor.apellido, "email":profesor.email, "profesion":profesor.profesion})
        return render(request, "Appcoder/editarProfesor.html", {"formulario":form, "profesor":profesor})
        
########### VBC ###########
    


class EstudianteList(LoginRequiredMixin, ListView):
    model=Estudiante
    template_name="AppCoder/leerEstudiantes.html"

class EstudianteDetalle(LoginRequiredMixin, DetailView):
    model=Estudiante
    template_name="Appcoder/estudiante_detalle.html"

class EstudianteCreacion(CreateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre', 'apellido', 'email']

class EstudianteUpdate(UpdateView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')
    fields=['nombre', 'apellido', 'email']

class EstudianteDelete(DeleteView):
    model = Estudiante
    success_url = reverse_lazy('estudiante_listar')

###### login logout register


def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=request.POST["username"]
            clave=request.POST["password"]

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:
                login(request, usuario)
                return render(request, 'AppCoder/inicio.html', {'mensaje':f"Bienvenido {usuario}"})
            else:
                return render(request, "AppCoder/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})
        else:
            return render(request, "AppCoder/login.html", {"formulario":form, "mensaje":"Usuario o contraseña incorrectos"})

                
    else:
        form=AuthenticationForm()
        return render(request, "AppCoder/login.html", {"formulario":form})


def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            form.save()
            return render(request, "AppCoder/inicio.html", {"mensaje":f"Usuario {username} creado correctamente"})
        else:
            return render(request, "AppCoder/register.html", {"formulario":form, "mensaje":"FORMULARIO INVALIDO"})

    else:
        form=UserRegisterForm()
        return render(request, "AppCoder/register.html", {"formulario":form})