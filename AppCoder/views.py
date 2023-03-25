from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *
from datetime import date
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here. 



def inicio (request):
    return render (request, "inicio.html")

# def cursos (request):
#     return render (request, "cursos.html")

# def profesores (request):
#     return render (request, "profesores.html")

# def estudiantes (request):
#     return render (request, "estudiantes.html")

# def entregables (request):
#     return render (request, "entregables.html")

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST) #aqui llega la informacion del html

        print(miFormulario)

        if miFormulario.is_valid():  #si paso la validacion de django

            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = CursoFormulario()

    return render(request, "cursos.html", {'miFormulario': miFormulario})

def profesores(request):
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])

            profesor.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = ProfesorFormulario()

    return render(request, "profesores.html", {'miFormulario':miFormulario})

def estudiantes(request):
    if request.method == 'POST':
        miFormulario = EstudianteFormulario(request.POST)

        print(miFormulario)
        

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'])

            estudiante.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = EstudianteFormulario()
        
    return render(request, "estudiantes.html", {'miFormulario':miFormulario})

def entregable(request):
    if request.method == 'POST':
        miFormulario = EntregableFormulario(request.POST)

        print(miFormulario)
        

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            print(informacion['fechaEntrega'])
            print(type(informacion['fechaEntrega']))

            entregable = Entregable (nombre = informacion['nombre'], fechaEntrega = informacion['fechaEntrega'], entregado = informacion['entregado'])

            entregable.save()

            return render(request, 'inicio.html')
    else:
        miFormulario = EntregableFormulario()
        
    return render(request, "entregable.html", {'miFormulario':miFormulario})

def busquedaCamada(request):
    return render(request, 'busquedaCamada.html')

def buscar(request):
    if request.GET["camada"]:
        camada = request.GET['camada']
        cursos = Curso.objects.filter(camada__icontains=camada)

        return render(request, 'resultadosBusqueda.html',{"cursos":cursos, "camada":camada})
    else:
        respuesta = "No eviaste datos."
    return HttpResponse(respuesta)

def leerProfesores(request):
    profesores = Profesor.objects.all() #para que traiga a todos los profesores de la tabla
    contexto = {"profesores":profesores}
    return render(request, "leerProfesores.html", contexto)

def leerCursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "leerCursos.html", contexto)

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()

    #para poder volver al menú

    profesores = Profesor.objects.all()
    contexto = {"profesores": profesores}

    return render(request, "leerProfesores.html", contexto)

def editarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    if request.method == 'POST':
        miFormulario = ProfesorFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            profesor.nombre = informacion['nombre']
            profesor.apellido = informacion['apellido']
            profesor.email = informacion['email']
            profesor.profesion = informacion['profesion']

            profesor.save()
            return render(request, "inicio.html")
    else:
        miFormulario = ProfesorFormulario(initial={'nombre':profesor.nombre,'apellido':profesor.apellido,'email':profesor.email,'profesion':profesor.profesion})

        return render(request, "editarProfesor.html", {"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})

class CursoList(ListView):
    model = Curso
    template_name = "curso_list.html"

class CursoDetalle(DetailView):
    model = Curso
    template_name = "curso_detalle.html"

class CursoCreacion(CreateView):
    model = Curso
    template_name = "curso_form.html"
    success_url = reverse_lazy("AppCoder:List")
    fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
    model = Curso
    success_url = "AppCoder/curso/list"
    template_name = "curso_form.html"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_confirm_delete.html"
    success_url = "AppCoder/curso/list"