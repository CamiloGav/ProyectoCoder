from django import forms
from django.forms import SelectDateWidget

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    profesion = forms.CharField(max_length=30)

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()

class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    fechaEntrega = forms.DateField(widget=SelectDateWidget(empty_label='Campo-vacio'))
    entregado = forms.BooleanField()