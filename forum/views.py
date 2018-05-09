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

    cur.nextset()


    cur.callproc('obtener_comentarios_publicacion', [id, ])
    comentarios = cur.fetchall()

    cur.nextset()

    cur.callproc('obtener_relevante_publicacion', [id, ])

    relevantes = cur.fetchall()

    cur.nextset()

    cur.callproc('obtener_indiferente_publicacion', [id, ])

    indiferentes = cur.fetchall()

    cur.nextset()

    cur.callproc('obtener_emocionante_publicacion', [id, ])

    emocionantes = cur.fetchall()

    cur.close()

    
    context = {
        'publicacion': publicacion[0],
        'comentarios': comentarios,
        'relevantes': relevantes[0],
        'indiferentes': indiferentes[0],
        'emocionantes': emocionantes[0],
        'id': id
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

    return HttpResponseRedirect(reverse('perfil:viewProfile'))




def deleteNoticia(request, id):
    template = loader.get_template('forum/editarNoticia.html')

    cur = connection.cursor()
    cur.callproc('eliminar_publicacion', [id,])
    cur.close

    return HttpResponseRedirect(reverse('perfil:viewProfile'))



def insertarComentario(request, id):
    template = loader.get_template('forum/detalleNoticia.html')

    print("ENTRA A COMENTARIOS")
    id_usuario = int(request.session['Usuario'])
    id_publicacion = id
    comentario = request.POST.get('comentario')

    cur = connection.cursor()
    cur.callproc('insertar_comentario_publicacion', [comentario, id_usuario, id_publicacion])
    cur.close

    #return HttpResponseRedirect("") 
    #redirect_to = reverse('forum:viewNoticia', kwargs={'id': id})
    #return redirect(redirect_to)
    #return HttpResponseRedirect(viewNoticia, id)
    return HttpResponseRedirect(reverse('forum:viewNoticia', args=[id]))

def calificarNoticiaRelevante(request, id):
    template = loader.get_template('forum/detalleNoticia.html')

    id_usuario = int(request.session['Usuario'])
    id_publicacion = id
    calificacion = "Relevante"

    cur = connection.cursor()
    cur.callproc('obtener_id_calificacion', [calificacion,])
    id_calificacion_tupla = cur.fetchall()
    

    id_calificacion = id_calificacion_tupla[0][0]

    
    cur.nextset()
    cur.callproc('calificar_publicacion', [id_publicacion,id_calificacion,id_usuario])

    cur.close

    return HttpResponseRedirect(reverse('forum:viewNoticia', args=[id])) 


def calificarNoticiaIndiferente(request, id):
    template = loader.get_template('forum/detalleNoticia.html')

    id_usuario = int(request.session['Usuario'])
    id_publicacion = id
    calificacion = "Indiferente"

    cur = connection.cursor()
    cur.callproc('obtener_id_calificacion', [calificacion,])
    id_calificacion_tupla = cur.fetchall()
    

    id_calificacion = id_calificacion_tupla[0][0]

    
    cur.nextset()
    cur.callproc('calificar_publicacion', [id_publicacion,id_calificacion,id_usuario])

    cur.close

    return HttpResponseRedirect(reverse('forum:viewNoticia', args=[id])) 


def calificarNoticiaEmocionante(request, id):
    template = loader.get_template('forum/detalleNoticia.html')

    id_usuario = int(request.session['Usuario'])
    id_publicacion = id
    calificacion = "Emocionante"

    cur = connection.cursor()
    cur.callproc('obtener_id_calificacion', [calificacion,])
    id_calificacion_tupla = cur.fetchall()
    

    id_calificacion = id_calificacion_tupla[0][0]

    
    cur.nextset()
    cur.callproc('calificar_publicacion', [id_publicacion,id_calificacion,id_usuario])

    cur.close

    return HttpResponseRedirect(reverse('forum:viewNoticia', args=[id])) 
    
