from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *

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

        if miFormulario.is_valid:  #si paso la validacion de django

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

        if miFormulario.is_valid:

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

        if miFormulario.is_valid:

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

        if miFormulario.is_valid:

            informacion = miFormulario.cleaned_data

            entregable = Entregable (nombre=informacion['nombre'], fecha=informacion['fecha'], entregado=informacion['entregado'])

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
