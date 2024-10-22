from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
	imagen = models.ImageField(upload_to='usuario', null=True, blank=True, default='usuario/user-default.png')

	def get_absolute_url(self):
		return reverse('home')
	pass
