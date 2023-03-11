from django.urls import path, include
from AppCoder import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('cursos', views.cursos, name='cursos'),
    path('profesores', views.profesores, name='profesores'),
    path('estudiantes', views.estudiantes, name='estudiantes'),
    path('entregable', views.entregable, name='entregable'),
    #path('cursoFormulario/', views.cursoFormulario, name='CursoFormulario'),
    #path('profesorFormulario/', views.profesorFormulario, name='ProfesorFormulario'),
    path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    path('buscar/', views.buscar)

]