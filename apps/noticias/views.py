from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Noticia, Categoria, Comentario
from .forms import NuevaCategoriaForm, NoticiaForm
from django.views.generic import ListView, DetailView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class CategoriaCreateView(CreateView):
	model = Categoria
	form_class = NuevaCategoriaForm
	template_name = 'noticias/crear_categoria.html'

	def get_success_url(self):
		next_url = self.request.GET.get('next')
		if next_url:
			return next_url
		return reverse_lazy('noticias:crear_noticia')

class CategoriaListView(ListView):
	model = Categoria
	template_name = 'noticias/categoria_list.html'
	context_object_name = 'categorias'

class CategoriaDeleteView(DetailView):
	model = Categoria
	template_name = 'noticias/categoria_confirm_delete.html'
	success_url = reverse_lazy('noticias:categoria_list')

# @login_required
# def Crear_Categoria(request):
# 	contexto = {'form': CategoriaForm()}

# 	if request.method == 'POST':
# 		form = CategoriaForm(request.POST)
# 		if form.is_valid():
# 			form.save()
# 			return redirect('noticias:crear_categoria')
# 		else:
# 			contexto['form'] = form

# 	return render(request, 'noticias/crear_categoria.html', contexto)

@login_required
def Crear_Noticia(request):
	contexto = {'form': NoticiaForm()}

	if request.method == 'POST':
		form = NoticiaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('noticias:listar')
		else:
			contexto['form'] = form

	return render(request, 'noticias/crear_noticia.html', contexto)

@login_required
def Listar_Noticias(request):
	contexto = {}

	id_categoria = request.GET.get('id',None)

	if id_categoria:
		n = Noticia.objects.filter(categoria_noticia = id_categoria)
	else:
		n = Noticia.objects.all() #RETORNA UNA LISTA DE OBJETOS

	contexto['noticias'] = n

	cat = Categoria.objects.all().order_by('nombre')
	contexto['categorias'] = cat

	return render(request, 'noticias/listar.html', contexto)

@login_required
def Detalle_Noticias(request, pk):
	contexto = {}

	n = Noticia.objects.get(pk = pk) #RETORNA SOLO UN OBEJTO
	contexto['noticia'] = n

	c = Comentario.objects.filter(noticia = n)
	contexto['comentarios'] = c

	return render(request, 'noticias/detalle.html',contexto)


@login_required
def Comentar_Noticia(request):

	com = request.POST.get('comentario',None)
	usu = request.user
	noti = request.POST.get('id_noticia', None)# OBTENGO LA PK
	noticia = Noticia.objects.get(pk = noti) #BUSCO LA NOTICIA CON ESA PK
	coment = Comentario.objects.create(usuario = usu, noticia = noticia, texto = com)

	return redirect(reverse_lazy('noticias:detalle', kwargs={'pk': noti}))

#{'nombre':'name', 'apellido':'last name', 'edad':23}
#EN EL TEMPLATE SE RECIBE UNA VARIABLE SEPARADA POR CADA CLAVE VALOR
# nombre
# apellido
# edad

'''
ORM

CLASE.objects.get(pk = ____)
CLASE.objects.filter(campos = ____)
CLASE.objects.all() ---> SELECT * FROM CLASE

'''