from django.conf.urls import url, include
from . import views

app_name = "home"



urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^errorLogin/$', views.errorLogin, name='errorLogin'),
    url(r'^servicio$', views.viewService, name='viewService'),
    url(r'^interes$', views.viewInteres, name='viewInteres'),
    url(r'^admin$', views.admin, name='admin'),
    url(r'^admin/agregarSitio$', views.agregarSitio, name='agregarSitio'),
    url(r'^admin/agregarUsuarios$', views.agregarUsuarios, name='agregarUsuarios'),
    url(r'^admin/editar/(?P<id>[0-9]+)$', views.editarSitio, name='editarSitio'),
    url(r'^admin/editarAux/(?P<id>[0-9]+)$', views.editarSitioAux, name='editarSitioAux'),
    url(r'^admin/eliminar/(?P<id>[0-9]+)$', views.eliminarSitio, name='eliminarSitio'),


    
    ]

