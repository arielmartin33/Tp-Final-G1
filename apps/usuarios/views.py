from .forms import RegistroForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib.auth.models import Group

# Create your views here.

class Registro(CreateView):
	#FORMULARIO DJANGO
	form_class = RegistroForm
	template_name = 'usuarios/registro.html'

	def form_valid(self, form):
		response = super().form_valid(form)
		messages.success(self.request, 'Usuario creado correctamente')
		group = Group.objects.get(name='Registrado')
		self.object.groups.add(group)
		#form.save()
		return redirect('usuarios:registro')

class LoginUsuario(LoginView):
	template_name = 'usuarios/login.html'

	def get_success_url(self):
		messages.success(self.request, 'Login Exitoso')
		return reverse_lazy('apps.usuarios:login')
	
class LogoutUsuario(LogoutView):
	template_name = 'usuarios/logout.html'

	def get_success_url(self):
		messages.success(self.request, 'Logout Exitoso')
		return reverse_lazy('apps.usuarios:logout')