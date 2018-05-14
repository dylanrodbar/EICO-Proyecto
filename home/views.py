from datetime import datetime

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
#from django.urls import reverse
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

import cv2
import os
import numpy as np
import Excel

def enviarCorreosElectronicos():
    send_mail('Prueba de envío de correos varios usuarios', 'Im Poppy', 'pdjango123@gmail.com', ['dylanrodbar97@gmail.com', 'josemorar96@gmail.com ', 'karizp14@gmail.com '])
    

def dividirListaGruposTres(lista):
    lista_retorno = []
    largo = 0
    return 0

def index(request):

    cur = connection.cursor()
    cur.callproc('obtener_publicaciones_recientes', [])
    publicaciones = cur.fetchall() 
    print(publicaciones)   

    enviarCorreosElectronicos()

    return render(request, 'home/index.html')


def errorLogin(request):
    template = loader.get_template('home/index.html')
    context = {
        'error': "El usuario o contraseña es incorrecto"
    }

    return HttpResponse(template.render(context, request))


def login(request):
    template = loader.get_template('home/header.html')
    context = {}
    username = request.POST.get('email')
    password = str(request.POST.get('password'))
    cur = connection.cursor()
    login = cur.callproc('iniciar_sesion', [username, password])
    login = cur.fetchall()
    cur.close
    if login == ():
        return HttpResponseRedirect(reverse('home:errorLogin'))
    else:
        request.session['Usuario'] = login[0][0]
        request.session['IdTipoUsuario'] = login[0][1]
        request.session['TipoUsuario'] = login[0][2]
        request.session['Mes'] = 1
        request.session['Anio'] = 1
        
        return HttpResponseRedirect(reverse('forum:viewEscuela'))
        # if login[0][1] == "Administrador":
        #    return HttpResponseRedirect(reverse('blog:noticias'))
        # elif login[0][1] == "Cliente":
        #    return HttpResponseRedirect(reverse('blogClient:noticias'))


def logout(request):
    template = loader.get_template('home/header.html')

    del request.session['Usuario']
    del request.session['TipoUsuario']
    del request.session['IdTipoUsuario']

    request.session.modified = True

    return HttpResponseRedirect(reverse('forum:viewEscuela'))


def viewService(request):
    template = loader.get_template('home/servicio.html')

    cur = connection.cursor()
    cur.callproc('obtener_servicios', [])
    servicios = cur.fetchall()
    cur.close

    context = {
        'servicios': servicios
    }
    return HttpResponse(template.render(context, request))


def viewInteres(request):
    template = loader.get_template('home/interes.html')

    cur = connection.cursor()
    cur.callproc('obtener_sitios_interes', [])
    sitios = cur.fetchall()
    cur.close

    context = {
        'sitiosinteres': sitios
    }
    return HttpResponse(template.render(context, request))


def admin(request):
    template = loader.get_template('home/admin.html')

    cur = connection.cursor()
    cur.callproc('obtener_sitios_interes', [])
    sitios = cur.fetchall()


    cur.nextset()

    cur.callproc('obtener_servicios', [])
    servicios = cur.fetchall()

    cur.nextset()
    cur.callproc('obtener_calendario', [])
    calendarios = cur.fetchall()
    cur.close

    context = {
        'sitiosinteres': sitios,
        'servicios': servicios,
        'calendarios': calendarios,
        'id': 0
    }
    return HttpResponse(template.render(context, request))


def agregarUsuarios(request):
    template = loader.get_template('home/admin.html')

    file = request.FILES.get("archivo")

    elementos_excel = Excel.manejar_excel(file)

    cur = connection.cursor()
    for i in (elementos_excel):
        usuario = i[0]
        contrasena = i[3]
        correo = i[1]
        media = 1
        tipo_usuario = int(i[2])
        cur.callproc('insertar_usuario', [usuario, contrasena, correo, media, tipo_usuario])
        cur.nextset()

    cur.close

    return HttpResponseRedirect(reverse('home:admin'))


def agregarSitio(request):
    template = loader.get_template('home/admin.html')
    titulo = request.POST.get('titulo-sitio')
    descripcion = request.POST.get('descripcion-sitio')
    print(titulo)
    print(descripcion)
    cur = connection.cursor()
    cur.callproc('insertar_sitio_interes', [titulo, descripcion])
    cur.close
    return HttpResponseRedirect(reverse('home:admin'))


def editarSitio(request, id):
    template = loader.get_template('home/editarsitio.html')
    context = {
        'id': id
    }
    return HttpResponse(template.render(context, request))


def editarSitioAux(request, id):
    template = loader.get_template('home/editarsitio.html')
    titulo = request.POST.get('titulo')
    contenido = request.POST.get('descripcion')
    cur = connection.cursor()
    cur.callproc('editar_sitio_interes', [id, titulo, contenido])
    cur.close
    return HttpResponseRedirect(reverse('home:admin'))


def eliminarSitio(request, id):
    template = loader.get_template('home/admin.html')
    context = {}
    cur = connection.cursor()
    cur.callproc('eliminar_sitio_interes', [id])
    cur.close

    return HttpResponseRedirect(reverse('home:admin'))


def agregarEvento(request):
    template = loader.get_template('home/admin.html')
    fecha = request.POST.get('fecha-evento')
    nombre = request.POST.get('nombre-evento')
    descripcion = request.POST.get('descripcion-evento')


    cur = connection.cursor()
    cur.callproc('insertar_calendario', [nombre, descripcion, fecha])
    cur.close
    return HttpResponseRedirect(reverse('home:admin'))


def editarEvento(request, id):
    template = loader.get_template('home/editarcalendario.html')
    context = {
        'id': id
    }
    return HttpResponse(template.render(context, request))

def editarEventoAux(request, id):
    template = loader.get_template('home/editarsitio.html')

    fecha = request.POST.get('fecha-evento')
    nombre = request.POST.get('nombre-evento')
    descripcion = request.POST.get('descripcion-evento')


    cur = connection.cursor()
    cur.callproc('editar_calendario', [id, nombre, descripcion, fecha])
    cur.close
    return HttpResponseRedirect(reverse('home:admin'))


def eliminarEvento(request, id):
    template = loader.get_template('home/admin.html')
    context = {}
    cur = connection.cursor()
    cur.callproc('eliminar_calendario', [id])
    cur.close

    return HttpResponseRedirect(reverse('home:admin'))
