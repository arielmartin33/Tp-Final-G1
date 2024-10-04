from django.urls import path
from .views import EditarUsuario
from . import views

app_name = 'usuarios'

urlpatterns = [
    
    path('registro/', views.Registro.as_view(), name = 'registro'),
    path('editar/', EditarUsuario.as_view(), name = 'editar')

   

]