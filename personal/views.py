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


# Create your views here.
def viewProfile(request):

    template = loader.get_template('personal/perfil.html')

    id_usuario = request.session['Usuario']

    cur = connection.cursor()
    cur.callproc('obtener_usuario_id', [id_usuario,])
    datos_usuario = cur.fetchall()
    cur.close

    datos_usuario_detalle = datos_usuario[0]

    context = {
        'datos_usuario': datos_usuario_detalle
    }

    return HttpResponse(template.render(context, request))

def editarPerfil(request):

    template = loader.get_template('personal/perfil.html')

    id_usuario = request.session['Usuario']

    nombre = request.POST.get('nombre')
    titulo = request.POST.get('titulo')
    puesto_actual = request.POST.get('puesto_actual')
    lugar_trabajo = request.POST.get('lugar_trabajo')
    correo_electronico = request.POST.get('correo_electronico')
    archivo = request.FILES.get("archivo")

    imagen_subida = cloudinary.uploader.upload(archivo)

    # obtiene la referencia que va a permitir mostrar la imagen en la aplicación
    imagen_subida_url = imagen_subida["secure_url"]

    cur = connection.cursor()
    cur.callproc('editar_usuario', [id_usuario, nombre, correo_electronico, titulo, puesto_actual, lugar_trabajo, imagen_subida_url])
    cur.close

    return HttpResponseRedirect(reverse('perfil:viewProfile'))



