

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
#from django.urls import reverse
from django.core.urlresolvers import reverse

from calendar import Calendar
import datetime


def obtener_nombre_mes(numero_mes):
    if numero_mes == 1:
        return "ENERO"
    elif numero_mes == 2:
        return "FEBRERO"
    elif numero_mes == 3:
        return "MARZO"
    elif numero_mes == 4:
        return "ABRIL"
    elif numero_mes == 5:
        return "MAYO"
    elif numero_mes == 6:
        return "JUNIO"
    elif numero_mes == 7:
        return "JULIO"
    elif numero_mes == 8:
        return "AGOSTO"
    elif numero_mes == 9:
        return "SEPTIEMBRE"
    elif numero_mes == 10:
        return "OCTUBRE"
    elif numero_mes == 11:
        return "NOVIEMBRE"
    elif numero_mes == 12:
        return "DICIEMBRE"

def obtener_mes_anio_actual():
    actual = datetime.datetime.now()
    mes_actual = actual.month
    anio_actual = actual.year
    dia_actual = actual.day
    return mes_actual, anio_actual, dia_actual

def obtener_dia_inicio_mes_anio(mes, anio):
    anio_matriz = Calendar().monthdayscalendar(anio, mes)
    primer_semana = anio_matriz[0]
    contador = 0
    for i in primer_semana:
        if i != 0:
            break
        else:
            contador += 1
    return contador


def obtener_numero_dias_mes(mes, anio):
    anio_matriz = Calendar().monthdayscalendar(anio, mes)
    ultima_semana = anio_matriz[-1]
    dias_mes = ultima_semana[0]
    for i in ultima_semana:
        if i != 0:
            dias_mes = i
        else:
            break
    return dias_mes


def obtener_datos_calendario(mes, anio):
    dia_inicio_mes = obtener_dia_inicio_mes_anio(mes, anio)
    numero_dias_mes = obtener_numero_dias_mes(mes, anio)
    suma_dias = dia_inicio_mes + numero_dias_mes
    dia_inicio_negativo = dia_inicio_mes * -1
    return dia_inicio_mes, numero_dias_mes, suma_dias, dia_inicio_negativo





# Create your views here.
def viewCalendar(request):
	template = loader.get_template('eicoCalendar/calendar.html')

	mes_actual, anio_actual, dia_actual = obtener_mes_anio_actual()
	dia_inicio_mes, numero_dias_mes, suma_dias, dia_inicio_negativo = obtener_datos_calendario(mes_actual, anio_actual)
	nombre_mes = obtener_nombre_mes(mes_actual)


	request.session['Mes'] = mes_actual
	request.session['Anio'] = anio_actual
	    
        

	cur = connection.cursor()
	cur.callproc('obtener_calendario', [])
	calendarios = cur.fetchall()
	cur.nextset()
	cur.close

	cur = connection.cursor() 

	context = {
		'calendarios': calendarios,
		'mesactual': nombre_mes,
		'diainiciomes': dia_inicio_mes,
		'numero_dias_mes': numero_dias_mes,
		'sumadias': suma_dias,
		'dianegativo': dia_inicio_negativo,
		'anioactual': anio_actual,
		'diaactual': dia_actual
	}
	return HttpResponse(template.render(context, request))

def obtenerSiguienteMes(request):
    template = loader.get_template('eicoCalendar/calendar.html')

    mes = request.session['Mes']
    anio = request.session['Anio']

    mes += 1
    if mes == 13:
        anio += 1
        mes = 1
	
    request.session['Mes'] = mes
    request.session['Anio'] = anio

    dia_inicio_mes, numero_dias_mes, suma_dias, dia_inicio_negativo = obtener_datos_calendario(mes, anio)
    nombre_mes = obtener_nombre_mes(mes)

    cur = connection.cursor()
    cur.callproc('obtener_calendario', [])
    calendarios = cur.fetchall()
    cur.close
    cur.nextset()

    context = {
		'calendarios': calendarios,
		'mesactual': nombre_mes,
		'diainiciomes': dia_inicio_mes,
		'numero_dias_mes': numero_dias_mes,
		'sumadias': suma_dias,
		'dianegativo': dia_inicio_negativo,
		'anioactual': anio
    }

    return HttpResponse(template.render(context, request))


def obtenerAnteriorMes(request):
    template = loader.get_template('eicoCalendar/calendar.html')

    mes = request.session['Mes']
    anio = request.session['Anio']

    mes -= 1
    if mes == 0:
        anio -= 1
        mes = 12
	
    request.session['Mes'] = mes
    request.session['Anio'] = anio

    dia_inicio_mes, numero_dias_mes, suma_dias, dia_inicio_negativo = obtener_datos_calendario(mes, anio)
    nombre_mes = obtener_nombre_mes(mes)

    cur = connection.cursor()
    cur.callproc('obtener_calendario', [])
    calendarios = cur.fetchall()
    cur.close
    cur.nextset()

    context = {
		'calendarios': calendarios,
		'mesactual': nombre_mes,
		'diainiciomes': dia_inicio_mes,
		'numero_dias_mes': numero_dias_mes,
		'sumadias': suma_dias,
		'dianegativo': dia_inicio_negativo,
		'anioactual': anio
    }

    return HttpResponse(template.render(context, request))
    