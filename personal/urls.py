from django.conf.urls import url, include
from . import views

app_name = "perfil"
urlpatterns = [ 
                url(r'^$', views.viewProfile, name='viewProfile'),
                url(r'editarPerfil/$', views.editarPerfil, name='editarPerfil'),
                url(r'agregarExpecienciaOTrabajo/$', views.agregarExperienciaOTrabajo, name='agregarExperienciaOTrabajo'),
                url(r'agregarEducacion/$', views.agregarEducacion, name='agregarEducacion'),
                

            ]