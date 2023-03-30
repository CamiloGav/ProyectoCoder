from django.shortcuts import render
from AppCoder.models import *
from django.http import HttpResponse
from AppCoder.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppCoder.forms import UserRegisterForm, UserEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
# Create your views here. 



# def inicio (request):
#     return render (request, "inicio.html")

# def cursos (request):
#     return render (request, "cursos.html")

# def profesores (request):
#     return render (request, "profesores.html")

# def estudiantes (request):
#     return render (request, "estudiantes.html")

# def entregables (request):
#     return render (request, "entregables.html")
@login_required
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

@login_required
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

@login_required
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

@login_required
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

@login_required
def leerCursos(request):
    cursos = Curso.objects.all()
    contexto = {"cursos": cursos}
    return render(request, "cursos_list.html", contexto)

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

#Clases para "Curso"
class CursoList(ListView):
    model = Curso
    template_name = "cursos_list.html"

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
    success_url = "/AppCoder/curso/list"
    template_name = "curso_form.html"
    fields = ['nombre', 'camada']

class CursoDelete(DeleteView):
    model = Curso
    template_name = "curso_confirm_delete.html"
    success_url = "/AppCoder/curso/list"

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contras = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contras)
            if user is not None:
                login(request, user)
                return render(request, "inicio.html", {"mensaje":f'Bienvenido {usuario}' })
            else:
                return render(request, "inicio.html", {"mensaje":f'Error, datos incorretos.' })
        else:
            return render(request, "inicio.html", {"mensaje": f'Formulario erroneo.'})
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

def register(request):
    if request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, "inicio.html", {"mensaje":'Usuario creado :)'})
    else:
        #form = UserCreationForm()
        form = UserRegisterForm()
    return render(request, "registro.html", {"form":form})

@login_required
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request, 'inicio.html', {"url": avatares[0].imagen.url})

@login_required
def editarPerfil(request):
    usuario =request.user
    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.first_name = informacion['first_name']
            usuario.last_name = informacion['last_name']
            if informacion['password1'] == informacion['password2']:
                usuario.password = make_password(informacion['password1'])
                usuario.save()
            else:
                return render(request, 'inicio.html', {'mensaje': 'Contraseña incorrecta'})
            return render(request, 'inicio.html')
    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})
        
    return render(request, "editarPerfil.html", {"miFormulario": miFormulario, "usuario":usuario})