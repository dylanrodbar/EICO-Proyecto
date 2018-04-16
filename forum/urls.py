from django.conf.urls import url, include
from . import views


app_name = "forum"

urlpatterns = [ 
                url(r'^escuela/$', views.viewEscuela, name='viewEscuela'),
                url(r'^escuela/nueva$', views.newEscuela, name='newEscuela'),
                
                url(r'^egresado/$', views.viewEgresado, name='viewEgresado'),  
                url(r'^egresado/nueva$', views.newEgresado, name='newEgresado'), 

                url(r'^insertarPost/$', views.insertarPost, name='insertarPost'),

                url(r'^editar/$', views.editNoticia, name='editNoticia'),

                url(r'^ver/(?P<id>[0-9]+)/$', views.viewNoticia, name="viewNoticia"),
                              
            ]