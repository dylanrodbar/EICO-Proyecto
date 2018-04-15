

from django.shortcuts import render

# Create your views here.
def viewProfile(request):
	return render(request, 'personal/perfil.html')