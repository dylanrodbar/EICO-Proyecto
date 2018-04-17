from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.urls import reverse

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

