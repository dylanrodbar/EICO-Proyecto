

from django.shortcuts import render

# Create your views here.
def viewCalendar(request):
	print("hols")
	return render(request, 'eicoCalendar/calendar.html')