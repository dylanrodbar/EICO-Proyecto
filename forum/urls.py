from django.conf.urls import url, include
from . import views


app_name = "forum"

urlpatterns = [ 
                url(r'^escuela/$', views.viewEscuela, name='viewEscuela'),
                url(r'^escuela/nueva$', views.newEscuela, name='newEscuela'),
                
                url(r'^egresado/$', views.viewEgresado, name='viewEgresado'),  
                url(r'^egresado/nueva$', views.newEgresado, name='newEgresado'), 

                url(r'^insertarPost/$', views.insertarPost, name='insertarPost'),

                url(r'^changePost/(?P<id>[0-9]+)/$', views.changePost, name='changePost'),

                url(r'^editar/(?P<id>[0-9]+)/$', views.editNoticia, name="editNoticia"),

                url(r'^eliminar/(?P<id>[0-9]+)/$', views.deleteNoticia, name="deleteNoticia"),

                url(r'^ver/(?P<id>[0-9]+)/$', views.viewNoticia, name="viewNoticia"),

                url(r'^insertarComentario/(?P<id>[0-9]+)/$', views.insertarComentario, name="insertarComentario"),
                              
            ]