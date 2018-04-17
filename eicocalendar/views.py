

from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db import connection
from django.urls import reverse

# Create your views here.
def viewCalendar(request):
	template = loader.get_template('eicoCalendar/calendar.html')

	cur = connection.cursor()
	cur.callproc('obtener_calendario', [])
	calendarios = cur.fetchall()
	cur.close

	context = {
		'calendarios': calendarios,
	}
	return HttpResponse(template.render(context, request))

