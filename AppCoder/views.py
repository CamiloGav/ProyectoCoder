from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

# Create your views here.

def curso(self):

    curso = Curso(nombre='Desarrollo Web', camada= 12345)
    curso.save()

    documentoDeTexto = f'---> Curso: {curso.nombre} ---> Camada : {curso.camada}'

    return HttpResponse(documentoDeTexto)
