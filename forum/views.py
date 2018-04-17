from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.urls import reverse
import cloudinary.uploader

cloudinary.config(
    cloud_name = 'poppycloud',
    api_key = '328358331617938',
    api_secret = 'z-7k70XpvP1dl1ZdiqVF0olXp7A'
)

def viewEscuela(request):
    template = loader.get_template('forum/escuela.html')

    cur = connection.cursor()
    cur.callproc('obtener_publicaciones_escuela', [])
    noticias = cur.fetchall()
    cur.close

    print(noticias)
    
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
    link_video = request.POST.get('video')
    file = request.FILES.get("archivo")

    embed_link_video = link_video.replace("watch?v=", "embed/")

    user = int(request.session['Usuario'])

    imagen_subida = cloudinary.uploader.upload(file)

    #obtiene la referencia que va a permitir mostrar la imagen en la aplicación
    imagen_subida_url = imagen_subida["secure_url"]

    cur = connection.cursor()
    cur.callproc('insertar_publicacion', [titulo, descripcion, embed_link_video, imagen_subida_url, user])
    cur.close

    return HttpResponseRedirect(reverse('forum:viewEscuela'))


def viewNoticia(request, id):

    template = loader.get_template('forum/detalleNoticia.html')

    cur = connection.cursor()
    cur.callproc('obtener_publicacion_id', [id, ])
    publicacion = cur.fetchall()

    print(publicacion)

    context = {
        'publicacion': publicacion[0]
    }

    return HttpResponse(template.render(context, request))



def editNoticia(request, id):
    template = loader.get_template('forum/editarNoticia.html')
    context = {
        "id": id,

    }
    return HttpResponse(template.render(context, request))


def changePost(request, id):
    template = loader.get_template('forum/editarNoticia.html')

    titulo = request.POST.get('titulo')
    descripcion = request.POST.get('descripcion')
    link_video = request.POST.get('video')
    file = request.FILES.get("archivo")

    embed_link_video = link_video.replace("watch?v=", "embed/")

    user = int(request.session['Usuario'])

    imagen_subida = cloudinary.uploader.upload(file)

    # obtiene la referencia que va a permitir mostrar la imagen en la aplicación
    imagen_subida_url = imagen_subida["secure_url"]

    cur = connection.cursor()
    cur.callproc('editar_publicacion', [id, titulo, descripcion, embed_link_video, imagen_subida_url])
    cur.close




def deleteNoticia(request, id):
    template = loader.get_template('forum/editarNoticia.html')

    cur = connection.cursor()
    cur.callproc('eliminar_publicacion', [id,])
    cur.close

    return HttpResponseRedirect(reverse('perfil:viewProfile'))

