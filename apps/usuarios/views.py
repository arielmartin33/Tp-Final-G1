from django.shortcuts import render
from django.views import generic
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserChangeForm
from .forms import RegistroForm
# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	success_url = reverse_lazy('login')
	template_name = 'usuarios/registro.html'

class EditarUsuario(generic.CreateView):
	#FORMULARIO DJANGO
	form_class = UserChangeForm
	template_name = 'usuarios/editar_perfil.html'
	success_url = reverse_lazy('home')