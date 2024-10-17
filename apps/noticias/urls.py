
from django.urls import path
from . import views
from .views import *

app_name = 'noticias'

urlpatterns = [
	
	path('', views.Listar_Noticias, name = 'listar'),

	path('Detalle/<int:pk>', views.Detalle_Noticias, name = 'detalle'),
	
	path('Comentario/', views.Comentar_Noticia, name = 'comentar'),
    
	path('Crear/', views.Crear_Noticia, name = 'crear_noticia'),
    
	path('noticia/categoria', CategoriaCreateView.as_view(), name = 'crear_categoria'),
    
	path('categoria/', CategoriaListView.as_view(), name = 'categoria_list'),
    
    path('categoria/<int:pk>', CategoriaDeleteView.as_view(), name = 'categoria_delete'),
	
]