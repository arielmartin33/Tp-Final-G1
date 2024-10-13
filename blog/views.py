from django.shortcuts import render
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse

#request 'es un diccionario que continuamente se va pasando entre el navegador y el servidor'

def Home(request):

	return render(request, 't_home.html')

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return HttpResponseRedirect(reverse('home'))  # Redirige a la página principal
    else:
        return HttpResponseRedirect(reverse('home'))  # Manejo de GET opcional


def Nosotros(request):

	return render(request, 't_nosotros.html')