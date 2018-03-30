from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.core.urlresolvers import reverse

# Create your views here.
def viewEscuela(request):
    template = loader.get_template('forum/escuela.html')

    cur = connection.cursor()
    cur.callproc('obtener_publicaciones_escuela', [])
    noticias = cur.fetchall()
    cur.close
    
    
    context = {
   	    'noticias': noticias 
    }
    return HttpResponse(template.render(context, request))

    #return render(request, 'forum/escuela.html')

def viewEgresado(request):
    template = loader.get_template('forum/egresado.html')

    cur = connection.cursor()
    cur.callproc('obtener_publicaciones_egresados', [])
    noticias = cur.fetchall()
    cur.close
    
    
    
    context = {
	    'egresados': noticias 
    }
    return HttpResponse(template.render(context, request))
    #return render(request, 'forum/egresado.html')

def newEgresado(request):
	return render(request, 'forum/nuevaNoticia.html')

def newEscuela(request):
	return render(request, 'forum/nuevaNoticia.html')

def insertarPost(request):
    template = loader.get_template('forum/nuevaNoticia.html')
    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    user = int(request.session['Usuario'])
    cur = connection.cursor()
    cur.callproc('insertar_publicacion', [titulo, descripcion, user])
    cur.close
    return HttpResponseRedirect(reverse('forum:viewEscuela'))
