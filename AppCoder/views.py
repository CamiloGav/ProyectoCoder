from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here. 

def curso(self):

    curso = Curso(nombre='Desarrollo Web', camada= 12345)
    curso.save()

    documentoDeTexto = f'---> Curso: {curso.nombre} ---> Camada : {curso.camada}'

    return HttpResponse(documentoDeTexto)

def inicio (request):
    return HttpResponse('Estamos en el Inicio')

def cursos (request):
    return HttpResponse('Estamos en el cursos')

def profesores (request):
    return HttpResponse('Estamos en el profesores')

def estudiantes (request):
    return HttpResponse('Estamos en el estudiantes')

def entregables (request):
    return HttpResponse('Estamos en el entregables')